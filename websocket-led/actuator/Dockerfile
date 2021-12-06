FROM python:3.9-slim-buster
COPY actuator.py /home
COPY requirements.txt /home
RUN pip3 install -r /home/requirements.txt
CMD ["python3","/home/actuator.py"]