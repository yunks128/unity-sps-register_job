#!/bin/bash

cwl_workflow_file_url=$1

# Create yaml files for the run
/home/ops/verdi/bin/python /cwl/create_cwl_yml.py

# run cwl workflow
# Question: what role does the /tmp dir play?
/home/ops/verdi/bin/cwl-runner --no-read-only --outdir /tmp /cwl/publish_job_status.cwl workflow_yaml.yml
/home/ops/verdi/bin/cwl-runner --no-read-only --outdir /tmp $cwl_workflow_file_url workflow_yaml.yml > cwl_outputs.txt
# TODO: use status code of cwl runner to determine success/fail
/home/ops/verdi/bin/cwl-runner --no-read-only --outdir /tmp /cwl/publish_job_status.cwl workflow_yaml.yml