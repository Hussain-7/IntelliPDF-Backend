FROM ubuntu:focal-20221130

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.9 \
    python3-pip \
    libsndfile1 \
    && \
    apt-get clean

RUN pip3 install numpy nltk openai async-timeout fastapi python-dotenv hypercorn

RUN pip3 install protobuf==3.20.0 grpcio grpcio-tools

RUN pip3 install requests redis


COPY . .

CMD ["hypercorn", "--bind", "0.0.0.0:4000", "main:app"]

EXPOSE 4000
