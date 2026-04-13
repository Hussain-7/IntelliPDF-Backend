# IntelliPDF Backend

Backend service for IntelliPDF, handling PDF ingestion, vector storage, and similarity search for chat-style document interactions.

## What It Does

- Accepts uploaded PDF metadata and stores embeddings in Pinecone
- Converts PDFs into chunked content for retrieval workflows
- Exposes endpoints for semantic search against stored document namespaces
- Supports the IntelliPDF frontend experience

## Stack

- FastAPI
- LangChain
- OpenAI Embeddings
- Pinecone

## Setup

Copy the example environment file and add your API keys:

```bash
cp .env.example .env
```

Required credentials include:

- `OPENAI_API_KEY`
- `PINECONE_API_KEY`

## Run

```bash
./start.sh
```

## API Endpoints

- `GET /` - health-style greeting endpoint
- `POST /save_file_in_vector_db` - ingest a PDF into Pinecone
- `POST /search_similar_data` - retrieve similar chunks for a namespace

## License

MIT
