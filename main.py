from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from langchain_community.embeddings.openai import OpenAIEmbeddings
from utils.langchain import convertPdfToJson
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")


# For this project I have already configured an index in pinecone with name 'intelli-pdf'
pinecone_index_name='intelli-pdf'
pc = Pinecone(api_key=pinecone_api_key)
index= pc.Index('intelli-pdf');
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

app = FastAPI()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s'
)


app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def home():
    return {'message': 'Hello👋 Developers💻'}


@app.post('/save_file_in_vector_db')
async def saveFileInVectorDB(fileId,fileUrl):
    logging.info("saving file in vector db...")
    try:
        page_level_docs = convertPdfToJson(fileUrl);
        PineconeVectorStore.from_documents(page_level_docs, embeddings, index_name=pinecone_index_name,namespace=fileId)
        return {'message' : 'File namespace created successfully', 'status' : 200 }
    except:
        return {'message' : 'Error saving file in vector db', 'status' : 500 }
    


@app.post('/search_similar_data')
def searchSimilarData(data:dict):
    logging.info("searching for similar data...")
    message = data.get('message', '')
    namespace = data.get('namespace', '')
    vectorStore= PineconeVectorStore.from_existing_index(index_name=pinecone_index_name,embedding=embeddings,namespace=namespace)
    results=vectorStore.similarity_search(message,2);
    logging.info(f'search result: \n{results[0].page_content}');
    finalArray=[]
    for result in results:
        finalArray.append(result.page_content)
    return {'data': finalArray, 'message' : 'similar docs found successfully', 'status' : 200 }   