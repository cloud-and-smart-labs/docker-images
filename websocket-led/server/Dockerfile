FROM python:3.9-slim-buster
WORKDIR /usr/src/app
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 7890
CMD [ "python3", "server.py"]