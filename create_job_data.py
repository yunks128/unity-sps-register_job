import json
import argpars

"""
Consumes job _context.json file from verdi directory and produces job_data.json to be used by SNS notification script.
"""

JOB_CONTEXT_FILE = "_context.json"
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
            job_context = json.loads(f.read())
        except json.decoder.JSONDecodeError:
            print("File is empty")
    job_params = job_context["job_specification"]["params"]
    workflow_inputs = [{"id": param["name"], "data": param["value"]} for param in job_params if param["destination"] == "context"] 
    workflow_outputs = []
    if args.outputs_file:
        with open(arg.outputs_file, 'r') as f:
            workflow_outputs = f.read()
    job_data = {
        "id": job_context["_prov"]["wasGeneratedBy"].split(":")[1], # get uuid from HySDS task ID of form task_id:uuid
        "inputs": workflow_inputs,
        "outputs": workflow_outputs,
        "status": args.status
    }
    with open(JOB_DATA_FILE, 'w') as f:
        f.write(json.dumps(job_data))


if __name__ == "__main__":
    main()