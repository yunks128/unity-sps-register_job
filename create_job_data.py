import json
import argparse

"""
Consumes job _context.json file from verdi directory and produces job_data.json to be used by SNS notification script.
"""

JOB_CONTEXT_FILE = "_context.json"
JOB_ID_FILE = "_job.json"
JOB_DATA_FILE = "job_data.json"

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--status", type=str, default="running")
    parser.add_argument("--outputs_file", type=str, default="")
    return parser.parse_args() 

def main():
    args = parse_args()
    with open(JOB_CONTEXT_FILE, 'r') as f:
        try:
            job_context_json = json.loads(f.read())
        except json.decoder.JSONDecodeError:
            print("Context file is empty")

    with open(JOB_ID_FILE, 'r') as f:
        try:
            job_id_json = json.loads(f.read())
        except json.decoder.JSONDecodeError:
            print("Job file is empty")
    job_params = job_context_json["job_specification"]["params"]
    workflow_inputs = [{"id": param["name"], "data": param["value"]} for param in job_params if param["destination"] == "context"] 
    workflow_outputs = []
    if args.outputs_file:
        with open(args.outputs_file, 'r') as f:
            workflow_outputs = json.loads(f.read())
    job_data = {
        "id": job_id_json["job_info"]["job_payload"]["payload_task_id"],
        "inputs": workflow_inputs,
        "outputs": workflow_outputs,
        "status": args.status
    }
    with open(JOB_DATA_FILE, 'w') as f:
        f.write(json.dumps(job_data))


if __name__ == "__main__":
    main()