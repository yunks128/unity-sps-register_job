#!/usr/bin/env python
import json
import yaml
import os

def get_inputs_from_context():
    """
    Parses the _context.json file and returns the user provided inputs
    :return: a dictionary of cwl key and user provided value
    """
    with open("_context.json", 'r') as f:
        try:
            job_context = json.loads(f.read())
        except json.decoder.JSONDecodeError:
            print('File is empty')
    print(f"job_context: {json.dumps(job_context, indent=2)}")
    workflow_inputs = dict()
    job_params = job_context.get("job_specification").get("params")

    for param in job_params:
        if param.get("destination") == "context":
            workflow_inputs[param.get("name")] = param.get("value")

    return workflow_inputs

def get_system_workflow_inputs():
    # Read in environment variales
    sys_wfl_inps = dict()
    sys_wfl_inps["staging_bucket"] = os.environ["STAGING_BUCKET"]
    sys_wfl_inps["client_id"] = os.environ["CLIENT_ID"]
    sys_wfl_inps["dapa_api"] = os.environ["DAPA_API"]
    return sys_wfl_inps

def create_yml():
    workflow_yaml = dict()
    # Reading in job inputs
    wfl_inps = get_inputs_from_context()
    workflow_yaml.update(wfl_inps)
    # setting other static / env values for workflow run
    sys_wfl_inps = get_system_workflow_inputs()
    workflow_yaml.update(sys_wfl_inps)
    # write out yaml
    with open(r'workflow_yaml.yml', 'w') as file:
        yml_document = yaml.dump(workflow_yaml, file)
    print(yml_document)


if __name__ == "__main__":
    create_yml()