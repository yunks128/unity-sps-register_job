#!/bin/bash

cwl_workflow_file_url=$1

# Create job environment from file
export $(xargs < job.env)

# Create yaml file for the run
python3 /cwl/create_cwl_yml.py

# run cwl workflow
# Question: what role does the /tmp dir play?
/home/ops/verdi/bin/cwl-runner --no-read-only --outdir /tmp $cwl_workflow_file_url workflow_yaml.yml