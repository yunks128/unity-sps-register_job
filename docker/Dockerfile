FROM hysds/pge-base:develop

USER root

RUN /home/ops/verdi/bin/pip install cwl-runner

# Need pyyaml for writing workflow yaml
RUN /home/ops/verdi/bin/pip install pyyaml

# TODO: create a location where science code is
RUN mkdir -p /tmp
WORKDIR /tmp

# copy in the script that runs cwl workflow
COPY run_cwl_workflow.sh .
RUN chmod +x run_cwl_workflow.sh
COPY create_cwl_yml.py .
RUN chmod +x create_cwl_yml.py

# TODO: change entrypoint, since we will not be running a bash script
ENTRYPOINT ["./run_cwl_workflow.sh"]
