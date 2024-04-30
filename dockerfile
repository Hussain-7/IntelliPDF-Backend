FROM ubuntu:focal-20221130

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.9 \
    python3-pip \
    libsndfile1 \
    && \
    apt-get clean

RUN pip3 install numpy openai async-timeout fastapi python-dotenv hypercorn

RUN pip3 install requests pypdf langchain_community langchain_pinecone langchain_text_splitters pinecone-client langchain-openai

RUN pip3 install langchain-pinecone langchain-openai langchain

COPY . .

# Create env file in 



CMD ["hypercorn", "--bind", "0.0.0.0:4000", "main:app"]

EXPOSE 4000
