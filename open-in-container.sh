docker build -t local/panduza-test-env .devcontainer
docker run -it --network=host -p=1883:1883 -v .:/tests local/panduza-test-env bash

