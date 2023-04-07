FROM ghcr.io/unity-sds/unity-sps-prototype/sps-hysds-pge-base:unity-v1.0.0

USER root

# Potentially hardcode env variables here or in run_cwl_workflow.sh
# For DEV
# ENV STAGING_BUCKET "uds-dev-cumulus-staging"
# ENV CLIENT_ID "71g0c73jl77gsqhtlfg2ht388c"
# ENV DAPA_API "https://1gp9st60gd.execute-api.us-west-2.amazonaws.com/dev"

# For TEST
ENV STAGING_BUCKET "uds-test-cumulus-staging"
ENV CLIENT_ID "6ir9qveln397i0inh9pmsabq1"
ENV DAPA_API "https://58nbcawrvb.execute-api.us-west-2.amazonaws.com/test"


# TODO: change entrypoint, since we will not be running a bash script
ENTRYPOINT ["/cwl/run_cwl_workflow.sh"]
