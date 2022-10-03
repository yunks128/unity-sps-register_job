FROM hysds/pge-base:develop

RUN /home/ops/verdi/bin/pip install cwl-runner

# copy in code needed for algorithm
RUN git clone ${REPO_URL_WITH_TOKEN} && \
   cd ${REPO_NAME} && \
   git checkout ${BRANCH}

# TODO: change entrypoint, since we will not be running a bash script
ENTRYPOINT ["/home/ops/verdi/bin/cwl-runner"]
