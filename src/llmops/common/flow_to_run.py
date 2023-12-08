import argparse
import os


_ROOT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "..")

def _build_category_path(category: str) -> str:
    return f"src/flows/{category}"

def _build_llmops_config_path(category_path: str) -> str:
    return f"{category_path}/llmops_config.json"

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

    return parser.parse_args()

def main(
    category: str,
    changed_files: str
):
    category_path = _build_category_path(category)
    standard_flow_rel_path = os.path.join(_ROOT_DIR, category_path, "flows", "standard")
    evaluation_flow_rel_path = os.path.join(_ROOT_DIR, category_path, "flows", "evaluation")

    standard_flow_candidates = os.listdir(standard_flow_rel_path)
    evaluation_flow_candidates = os.listdir(evaluation_flow_rel_path)

    standard_flows = _get_flows_from_candidates(standard_flow_candidates, standard_flow_rel_path)
    evaluation_flows = _get_flows_from_candidates(evaluation_flow_candidates, evaluation_flow_rel_path)
    # check if the standard flows have flow.dag.yaml files under them

    print(f"changed_files: {changed_files}")
    print(f"standard_flows: {standard_flows}")
    print(f"evaluation_flows: {evaluation_flows}")


if __name__ == "__main__":
    args = _get_args()
    main(
        category=args.category,
        changed_files=args.changed_files
    )
