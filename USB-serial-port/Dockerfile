FROM python:3.9-slim-buster
WORKDIR /usr/src/app
COPY . .
RUN pip install pyserial
CMD [ "python3", "read_serial_port.py"]