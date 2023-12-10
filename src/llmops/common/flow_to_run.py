import argparse
import os

from llmops.common.logger import llmops_logger

logger = llmops_logger("flows_to_run")


_ROOT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "..")

def _build_category_path(category: str) -> str:
    return f"src/flows/{category}"

def _build_subflow_reference(flow_type: str, flow: str) -> str:
    return f"flows/{flow_type}/{flow}"

def _build_subflow_path(category_path: str, flow: str) -> str:
    return f"{category_path}/flows/{flow}"

def _write_flows_to_run(flows_to_run: list[str], output_file_name: str):
    output_str = ",".join(flows_to_run)
    with open(output_file_name, "w") as f:
        f.write(output_str)

def _get_flows_from_candidates(
    candidates: list[str],
    path: str
) -> list[str]:
    flows = []
    for flow in candidates:
        flow_path = os.path.join(path, flow)
        if os.path.isdir(flow_path):
            if "flow.dag.yaml" in os.listdir(flow_path):
                flows.append(flow)
    return flows

def _get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--category",
        type=str,
        help="The category of the flow",
        required=True,
    )
    parser.add_argument(
        "--changed_files",
        type=str,
        help="The list of changed files",
        required=True,
    )
    parser.add_argument(
        "--default_subflow",
        type=str,
        help="The default subflow to run",
        required=True,
    )
    parser.add_argument(
        "--output_file_name",
        type=str,
        help="The name of the output file",
        required=True,
    )

    return parser.parse_args()

def main(
    category: str,
    changed_files: str,
    output_file_name: str,
    default_subflow: str,
):
    changed_files = changed_files.split(" ")

    category_path = _build_category_path(category)
    standard_flow_rel_path = os.path.join(_ROOT_DIR, category_path, "flows", "standard")
    evaluation_flow_rel_path = os.path.join(_ROOT_DIR, category_path, "flows", "evaluation")

    standard_flow_candidates = os.listdir(standard_flow_rel_path)
    evaluation_flow_candidates = os.listdir(evaluation_flow_rel_path)

    standard_flows = _get_flows_from_candidates(standard_flow_candidates, standard_flow_rel_path)
    evaluation_flows = _get_flows_from_candidates(evaluation_flow_candidates, evaluation_flow_rel_path)
    # check if the standard flows have flow.dag.yaml files under them

    standard_flow_paths = [_build_subflow_path(category_path, flow) for flow in standard_flows]
    evaluation_flow_paths = [_build_subflow_path(category_path, flow) for flow in evaluation_flows]

    logger.info(f"standard_flows: {standard_flows}")
    logger.info(f"evaluation_flows: {evaluation_flows}")

    for _, evaluation_flow_path in zip(evaluation_flows, evaluation_flow_paths):
        # if any of the eval flows have changed then we run all the standard flows
        if evaluation_flow_path in changed_files:
            logger.info(f"Found changed evaluation flow: {evaluation_flow_path}. Running all standard flows.")
            _write_flows_to_run(
                [_build_subflow_reference("standard", standard_flow) for standard_flow in standard_flows],
                output_file_name
            )

    flows_to_run = []
    for standard_flow, standard_flow_path in zip(standard_flows, standard_flow_paths):
        if standard_flow_path in changed_files:
            logger.info(f"Found changed standard flow: {standard_flow}")
            flows_to_run.append(_build_subflow_reference("standard", standard_flow))

    if flows_to_run:
        _write_flows_to_run(flows_to_run, output_file_name)
        return

    logger.info("No flows to run")
    _write_flows_to_run([default_subflow], output_file_name)

if __name__ == "__main__":
    args = _get_args()
    main(
        category=args.category,
        changed_files=args.changed_files,
        output_file_name=args.output_file_name,
        default_subflow=args.default_subflow,
    )
