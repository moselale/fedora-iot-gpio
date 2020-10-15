FROM fedora:latest

# imposta working directory
WORKDIR /code

RUN  dnf -y update
RUN  dnf -y install libgpiod-utils python3-libgpiod

# copia codice sorgente
COPY src/ .