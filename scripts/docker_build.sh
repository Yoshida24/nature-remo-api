#!/usr/bin/env bash

# exit on error
set -e

# add env
set -a
source .env
set +a

# build dockerfile
docker build . \
    -t nature_remo_api \
    -f app/docker/Dockerfile \
    --build-arg nature_access_token=${NATURE_ACCESS_TOKEN} \
    --build-arg nature_appearance=${NATURE_APPEARANCE} \
    --build-arg line_notify_token=${LINE_NOTIFY_TOKEN}
