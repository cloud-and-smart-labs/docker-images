FROM python:3.9-slim-buster
WORKDIR /usr/src/app
COPY ./fetch.py .
CMD [ "python3", "./fetch.py" ]