#!/bin/bash

openai_api_key=""

get_args () {
    while getopts o: flag; do
        case "${flag}" in
            o) openai_api_key=${OPTARG};;
        esac
    done
}

run () {
    # create connection to openai
    pf connection create -f ./connections/oai_connection.yml \
        --set api_key="${openai_api_key}"
}

get_args

# validate the arguments are all set
if [ -z "$openai_api_key" ]; then
    echo "Please provide the openai api key"
    exit 1
fi

run