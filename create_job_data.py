import json
import yaml
import argparse
import os

"""
Consumes job _context.json file from verdi directory and produces job_data.json to be used by SNS notification script.
"""

OUTPUT_DIR = os.getcwd()
JOB_CONTEXT_FILE = "_context.json"
JOB_ID_FILE = "_job.json"
JOB_DATA_FILE_NAME = "job_data.json"
CWL_INPUT_YAML_FILE_NAME = "publish_job_status.yml"

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--status", type=str, default="running")
    parser.add_argument("--outputs_file", type=str, default="")
    return parser.parse_args() 

def create_cwl_input_yaml(job_data_file_path):
    cwl_input_dict = {
        "job_data": {
            "class": "File",
            "path": job_data_file_path
        }
    }
    with open(CWL_INPUT_YAML_FILE_NAME, 'w') as f:
        yaml.dump(cwl_input_dict, f)


def main():
    args = parse_args()

    # read in job context file from verdi container
    with open(JOB_CONTEXT_FILE, 'r') as f:
        try:
            job_context_json = json.loads(f.read())
        except json.decoder.JSONDecodeError:
            print("Context file is empty")

    # read in file from verdi container that has the job id
    with open(JOB_ID_FILE, 'r') as f:
        try:
            job_id_json = json.loads(f.read())
        except json.decoder.JSONDecodeError:
            print("Job file is empty")

    # construct list of CWL inputs from context file
    job_params = job_context_json["job_specification"]["params"]
    workflow_inputs = [{"id": param["name"], "data": param["value"]} for param in job_params if param["destination"] == "context"] 

    # construct list of CWL outputs from given outputs file
    workflow_outputs = []
    if args.outputs_file:
        with open(args.outputs_file, 'r') as f:
            workflow_outputs = json.loads(f.read())

    # contstruct final job data json object
    job_data = {
        "id": job_id_json["job_info"]["job_payload"]["payload_task_id"],
        "inputs": workflow_inputs,
        "outputs": workflow_outputs,
        "status": args.status
    }

    # write out job data json object
    job_data_file_path = f'{OUTPUT_DIR}/{JOB_DATA_FILE_NAME}'
    with open(job_data_file_path, 'w') as f:
        f.write(json.dumps(job_data)) 
    
    # create cwl input yaml file for job data publishing workflow
    create_cwl_input_yaml(job_data_file_path)


if __name__ == "__main__":
    main()