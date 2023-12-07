from pathlib import Path
import importlib.util
from promptflow import PFClient


package_name = "llmops_tool"


def list_package_tools():
    """
    List the meta of all tools in the package.
    The key of meta dict is the module name of tools and value is the meta data of the tool.
    """
    # This function is auto generated by pf CLI, please do not modify manually.
    tools = {}
    pf_client = PFClient()
    script_files = Path(__file__).parent.glob("**/*.py")
    for file in script_files:
        if not str(file).endswith("__init__.py"):
            module_name = f'{package_name}.{Path(file).stem}'

            # Load the module from the file path
            spec = importlib.util.spec_from_file_location(module_name, file)
            module = importlib.util.module_from_spec(spec)

            # Load the module's code
            spec.loader.exec_module(module)
            tools.update(pf_client._tools.generate_tool_meta(module))
    return tools