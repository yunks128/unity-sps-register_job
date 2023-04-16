#!/bin/bash

cwl_workflow_file_url=$1

# Create yaml files for the run
python3 /cwl/create_cwl_yml.py
sudo python3 /cwl/create_job_data.py --status running

# run cwl workflow
# Question: what role does the /tmp dir play?
/home/ops/verdi/bin/cwl-runner /cwl/publish_job_status.cwl /cwl/publish_job_status.yml
/home/ops/verdi/bin/cwl-runner --no-read-only --outdir /tmp $cwl_workflow_file_url workflow_yaml.yml > cwl_outputs.txt
sudo python3 /cwl/create_job_data.py --status succeeded --outputs_file cwl_outputs.txt
/home/ops/verdi/bin/cwl-runner /cwl/publish_job_status.cwl /cwl/publish_job_status.yml