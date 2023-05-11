FROM ghcr.io/unity-sds/unity-sps-prototype/sps-hysds-pge-base-develop:develop

USER root

# Potentially hardcode env variables here or in run_cwl_workflow.sh
# For DEV
ENV STAGING_BUCKET "uds-dev-cumulus-staging"
ENV CLIENT_ID "71g0c73jl77gsqhtlfg2ht388c"
ENV DAPA_API "https://1gp9st60gd.execute-api.us-west-2.amazonaws.com/dev"

COPY ./job.env .

# TODO: change entrypoint, since we will not be running a bash script
ENTRYPOINT ["/cwl/run_cwl_workflow.sh"]
