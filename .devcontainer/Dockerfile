FROM ubuntu:22.04

# Attach to the repository
LABEL org.opencontainers.image.source https://github.com/Panduza/panduza-py

# Install Packages
RUN apt-get update && DEBIAN_FRONTEND=noninteractive TZ=Europe/Paris \
    apt-get -y install \
        python3 python3-pip \
        git

# 
RUN pip3 install    'git+https://github.com/Panduza/panduza-py@main'

# 
RUN pip3 install    robotframework
RUN pip3 install    PyHamcrest

#
WORKDIR /platform
