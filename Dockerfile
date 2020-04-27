FROM jjanzic/docker-python3-opencv
COPY mojo.py /mojo.py
ENTRYPOINT ["python", "/mojo.py"]

