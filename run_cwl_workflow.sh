#!/bin/bash

cwl_workflow_file_url = $0

# Create yaml file for the run
python create_cwl_yml.py

# run cwl workflow
# Question: what role does the /tmp dir play?
cwltool --no-read-only --outdir /tmp $cwl_workflow_file_url workflow_yaml.yml