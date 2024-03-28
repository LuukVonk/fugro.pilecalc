# To build an image using this Dockerfile you must expicitly pass the following
# build-time variables when calling 'docker build':
#   * PARAPY_PYPI_USERNAME: username for the ParaPy PyPI server
#   * PARAPY_PYPI_PASSWORD: password for the ParaPy PyPI server

#---------------------------
FROM docker.parapy.nl/parapy-cloud-app:latest as parent
# If a specific (Python) version is required, `latest` should be updated - e.g.:
# FROM docker.parapy.nl/parapy-cloud-app:3.11 as parent

#---------------------------
FROM parent as builder

RUN mkdir -p /tmp/build
WORKDIR /tmp/build
COPY . ./

RUN python3 -m pip install build
RUN python3 -m build --wheel --outdir wheelhouse

#---------------------------
FROM parent

ARG PARAPY_PYPI_USERNAME
ARG PARAPY_PYPI_PASSWORD
ARG PARAPY_APPLICATION_APP_MODULE=fpc.main
ARG PARAPY_APPLICATION_PORT=8000

COPY --from=builder /tmp/build/wheelhouse/* /tmp/build/wheelhouse/

RUN python3 -m pip install "$(ls /tmp/build/wheelhouse/fpc-*.whl)" \
    --no-cache-dir \
    --no-input \
    --index-url https://${PARAPY_PYPI_USERNAME}:${PARAPY_PYPI_PASSWORD}@pypi.parapy.nl/simple/

ENV PARAPY_APPLICATION_APP_MODULE=$PARAPY_APPLICATION_APP_MODULE
ENV PARAPY_APPLICATION_PORT=$PARAPY_APPLICATION_PORT
EXPOSE $PARAPY_APPLICATION_PORT

CMD uvicorn $PARAPY_APPLICATION_APP_MODULE:app --host 0.0.0.0 --port $PARAPY_APPLICATION_PORT
