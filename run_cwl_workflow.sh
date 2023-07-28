#!/bin/bash

cwl_workflow_file_url=$1

# Create yaml file for the run
python3 /cwl/create_cwl_yml.py

# run cwl workflow
# Question: what role does the /tmp dir play?
/home/ops/verdi/bin/cwl-runner --no-read-only --tmpdir-prefix /stage/ --outdir /tmp $cwl_workflow_file_url workflow_yaml.yml