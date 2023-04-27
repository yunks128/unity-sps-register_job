FROM ghcr.io/unity-sds/unity-sps-prototype/sps-hysds-pge-base:develop

USER root

ENV STAGING_BUCKET "uds-test-cumulus-staging"
ENV CLIENT_ID "6ir9qveln397i0inh9pmsabq1"
ENV DAPA_API "https://58nbcawrvb.execute-api.us-west-2.amazonaws.com/test"


# TODO: change entrypoint, since we will not be running a bash script
ENTRYPOINT ["/cwl/run_cwl_workflow.sh"]
