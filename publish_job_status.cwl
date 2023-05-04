cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["/usr/app/publish_job.py"]
hints:
    DockerRequirement:
        dockerPull: ghcr.io/unity-sds/unity-sps-prototype/sps-job-publisher:unity-v0.0.1
requirements:
    NetworkAccess:
        networkAccess: true

inputs:
    job_id:
        type: string
        inputBinding:
            position: 1
            prefix: --job_id
    job_status:
        type: string
        inputBinding:
            position: 2
            prefix: --job_status
    job_inputs:
        type: string
        inputBinding:
            position: 3
            prefix: --job_inputs
    job_outputs:
        type: string
        default: "[]"
        inputBinding:
            position: 4
            prefix: --job_outputs
    tags:
        type: string
        default: "{}"
        inputBinding:
            position: 5
            prefix: --tags
    auth_method:
        type: string
        default: iam
        inputBinding:
            position: 6
            prefix: --aws_auth_method
outputs:
    results:
        type: stdout
    errors:
        type: stderr
stdout: "publish_job_status_stdout.txt"
stderr: "publish_job_status_stderr.txt"
