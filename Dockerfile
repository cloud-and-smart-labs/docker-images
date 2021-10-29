FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3
ADD fetch.py /home/fetch.py
CMD ["/home/fetch.py"]
ENTRYPOINT ["python3"]