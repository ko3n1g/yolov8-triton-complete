# Getting started

This project provides fully self-contained OCI images for a triton-server-client setup. The triton base image has been chosen for it's compatibility to CUDA 11.8.

## Building images

For triton-server, run:

```bash
docker build -f docker/Dockerfile.tritonserver -t tritonserver .
```

For triton-client, run:

```bash
docker build -f docker/Dockerfile.tritonclient -t tritonclient .
```

## Running containers

First, spin up the server:

```bash
docker run --rm -p 8000:8000 tritonserver
```

Next, let the client send a request to it:

```bash
docker run -v runs --rm --network=host tritonclient
```
