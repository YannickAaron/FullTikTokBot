FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install chromium-browser=87.0.4280.66-0ubuntu0.18.04.1

#https://stackoverflow.com/questions/58134793/error-while-loading-shared-libraries-libnss3-so-while-running-gtlab-ci-job-to
RUN apt-get -y install xvfb

COPY ./DockerBuilds/x86_64/requirements.txt /install/requirements.txt

RUN pip3 install -r /install/requirements.txt

RUN mkdir /chromedriver

COPY ./DockerBuilds/x86_64/chromedriver_linux-x64/chromedriver /chromedriver/chromedriver
RUN mv /chromedriver/chromedriver /usr/lib/chromium-browser/chromedriver

# Add a /app volume
VOLUME ["/app"]

WORKDIR /app

ENTRYPOINT [ "python3" ]

#what to start
CMD [ "dockerSeleniumTest.py" ]
#CMD [ "dockerTest.py" ]
