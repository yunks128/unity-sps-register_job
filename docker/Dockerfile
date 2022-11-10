FROM hysds/pge-base:develop

USER root

RUN /home/ops/verdi/bin/pip install cwl-runner

# Need pyyaml for writing workflow yaml
RUN /home/ops/verdi/bin/pip install pyyaml

# TODO: create a location where science code is
RUN mkdir -p /cwl

# copy in the script that runs cwl workflow
COPY run_cwl_workflow.sh /cwl
RUN chmod +x /cwl/run_cwl_workflow.sh
COPY create_cwl_yml.py /cwl
RUN chmod +x /cwl/create_cwl_yml.py

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
