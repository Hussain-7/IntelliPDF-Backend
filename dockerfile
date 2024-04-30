FROM ubuntu:focal-20221130

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.9 \
    python3-pip \
    libsndfile1 \
    && \
    apt-get clean

RUN pip3 install numpy openai async-timeout fastapi python-dotenv hypercorn

RUN pip3 install requests pypdf langchain_community langchain_text_splitters os

COPY . .

CMD ["hypercorn", "--bind", "0.0.0.0:4000", "main:app"]

EXPOSE 4000
