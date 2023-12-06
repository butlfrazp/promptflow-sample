# LLM-Ops Tool

The directory structure in the package tool is as follows:
```python
llmops_tool
│   setup.py                # This file contains metadata about your project like the name, version.
│
└───llmops_tool      # This is the source directory. All of your project’s source code should be placed in this directory.
        langchain_chain.py  # The source code of tools. Using the @tool decorator to identify the function as a tool.
        utils.py            # Utility functions for the package. A method for listing all tools defined in the package is generated in this file.
        __init__.py
```

Please refer to [tool doc](https://microsoft.github.io/promptflow/how-to-guides/develop-a-tool/index.html) for more details about how to deploy a tool.

## Getting Started

### Building the package

To build the package, run the following command:

```bash
python setup.py sdist bdist_wheel
```
