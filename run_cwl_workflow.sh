#!/bin/bash

cwl_workflow_file_path = $0

# Create yaml file for the run
python create_cwl_yml.py

# run cwl workflow
# Question: what role does the /tmp dir play?
cwltool --no-read-only --outdir /tmp /some/location/$cwl_workflow_file_path workflow_yaml.yml