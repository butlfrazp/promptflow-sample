#!/bin/bash

azure_openai_api_key=""
azure_openai_api_base=""

while getopts "k:b:" flag; do
    case "${flag}" in
        k) azure_openai_api_key=${OPTARG};;
        b) azure_openai_api_base=${OPTARG};;
    esac
done

run () {
    # create connection to openai
    pf connection create -f ./connections/aoai_connection.yaml \
        --set api_key="${azure_openai_api_key}" \
        --set api_base="${azure_openai_api_base}"
}

# validate the arguments are all set
if [ -z "$azure_openai_api_key" ] || [ -z "$azure_openai_api_base" ]; then
    echo "Please provide the following arguments: -k <azure_openai_api_key> -b <azure_openai_api_base>"
    exit 1
fi

run