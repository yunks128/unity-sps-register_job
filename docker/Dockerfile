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

# TODO: change entrypoint, since we will not be running a bash script
ENTRYPOINT ["/cwl/run_cwl_workflow.sh"]
