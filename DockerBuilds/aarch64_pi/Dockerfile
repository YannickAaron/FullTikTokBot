FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

RUN  apt-get -s install chromium-browser=1:85.0.4183.83-0ubuntu0.20.04.2

COPY ../../app/config/requirements.txt /install/requirements.txt

RUN pip3 install -r /install/requirements.txt

# Add a /app volume
VOLUME ["/app"]

WORKDIR /app

ENTRYPOINT [ "python3" ]

#what to start
CMD [ "dockerTest.py" ]