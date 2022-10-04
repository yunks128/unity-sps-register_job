FROM hysds/pge-base:develop

RUN /home/ops/verdi/bin/pip install cwl-runner

# Need pyyaml for writing workflow yaml
RUN pip install pyyaml

# TODO: create a location where science code is
RUN mkdir /some/location
WORKDIR /some/location

# copy in the script that runs cwl workflow
RUN cp ../run_cwl_workflow.sh .
RUN chmod +x run_cwl_workflow.sh
RUN cp ../create_cwl_yml.sh .
RUN chmod +x create_cwl_yml.sh

# TODO: change entrypoint, since we will not be running a bash script
ENTRYPOINT ["/home/ops/verdi/bin/cwl-runner"]
