# Promptflow LLM-Ops Sample <!-- omit in toc -->

## Overview <!-- omit in toc -->

- [Documentation](#documentation)
- [Deployment](#deployment)
- [Pipeline](#pipeline)
- [Reports](#reports)
- [Local Execution](#local-execution)
  - [Contributing](#contributing)
  - [Trademarks](#trademarks)
  - [Code of Conduct](#code-of-conduct)
  - [License](#license)


## Folder structure

Use cases are defined under 'src/flows/<dataset-category>'.
Each use case (set of Prompt Flow standard and evaluation flows) should follow the folder structure as shown here:

- configs          : It contains data, deployment, and prompt flow data mapping related configuration files.
- data             : This folder contains data files related to Prompt Flow standard and evaluation flow
- environment      : It contains a Conda file for python package dependencies needed for deployment environment.
- flows            : It should contain minimally two folder - one for standard Prompt Flow related files and another for Evaluation flow related file. There can be multiple evaluation flow related folders.
- tests            : contains unit tests for the flows

Additionally, there is a llmops_config.json file that refers to important infrastructure and flow related information. There is also a sample-request.json file containing test data for testing endpoints after deployment.

- The '.github' folder contains the Github workflows for the platform as well as the use-cases.

- The 'docs' folder contains documentation for step-by-step guides for both Azure DevOps and Github Workflow related configuration.

- The 'src/flows' folder contains all the code related to flow execution, evaluation and deployment.

- The 'src/llmops' folder contains all the code related to the LLM-Ops execution, evaluation and deployment.
