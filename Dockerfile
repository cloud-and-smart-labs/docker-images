FROM python:3
WORKDIR /usr/src/app
COPY ./fetch.py .
CMD [ "python", "./fetch.py" ]