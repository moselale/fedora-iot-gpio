FROM fedora:latest
RUN  dnf -y update
RUN  dnf -y install libgpiod-utils python3-libgpiod