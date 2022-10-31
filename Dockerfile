FROM python:3.8

ARG container_name
ENV CONTAINER_NAME $container_name

WORKDIR /$CONTAINER_NAME

RUN curl https://sh.rustup.rs -y -sSf | sh

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD [ "python3", "server.py"]
