from setuptools import find_packages, setup
from typing import List

PACKAGE_NAME = "llmops_tool"

def parse_requirements(file_name: str) -> List[str]:
    with open(file_name) as f:
        return [
            require.strip() for require in f
            if require.strip() and not require.startswith('#')
        ]

setup(
    name=PACKAGE_NAME,
    version="1.0.1",
    description="This is my tools package",
    packages=find_packages(),
    entry_points={
        "package_tools": ["langchain_chain = llmops_tool.utils:list_package_tools"],
    },
    install_requires=parse_requirements("requirements.txt"),
)