FROM fedora:latest

# imposta working directory
WORKDIR /code

# copy the dependencies file to the working directory
#COPY requirements.txt .

# install dependencies
RUN pip install libgpiod-utils python3-libgpiod flask flask_restful

# copia codice sorgente
COPY src/ .

EXPOSE 5000
# command to run on container start
CMD [ "python3", "./main.py" ]