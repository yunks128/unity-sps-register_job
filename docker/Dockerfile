FROM hysds/pge-base:develop

RUN /home/ops/verdi/bin/pip install cwl-runner

# COPY ./sounder_sips/ /src

ENTRYPOINT ["/home/ops/verdi/bin/cwl-runner"]
