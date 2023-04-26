cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["/usr/app/publish_sns.py"]
hints:
    DockerRequirement:
        dockerPull: ghcr.io/unity-sds/unity-sps-prototype/sps-job-publisher:unity-v0.0.1
requirements:
    InitialWorkDirRequirement:
        listing:
            - $(inputs.job_data)
inputs:
    job_data:
        type: File
        inputBinding:
            position: 1
            valueFrom: $(self.basename)
    auth_method:
        type: string
        default: iam
        inputBinding:
            position: 2
            prefix: --aws_auth_method
outputs:
    results:
        type: stdout
    errors:
        type: stderr
stdout: "publish_job_status_stdout.txt"
stderr: "publish_job_status_stderr.txt"