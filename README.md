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

## Getting Started

### Creating Connections

Connections are used to securely connect to external resources such as OpenAI or Azure AI Search.
To create a connection locally, you can use the following command:

```bash
# cd into /src

./scripts/create-connection.sh -o <your-openai-api-key>
```

This will create a new connection called **oai** based on the [oai_connection.yaml](src/connections/oai_connection.yaml) file.

### Running a Standard Flow

To run a flow locally, you can use the following command:

```bash
python -m llmops.common.local_prompt_pipeline \
    --env_name pr \
    --data_purpose pr_data \
    --output_file sample.txt \
    --flow_to_execute flows/category_1
```

### Running an Evaluation Flow

To run an evaluation flow locally, you can use the following command:

```bash
python -m llmops.common.local_prompt_eval \
    --env_name pr \
    --data_purpose pr_data \
    --run_id "['run_id_1', 'run_id_2']" \
    --flow_to_execute flows/category_1
```
