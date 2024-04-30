from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from utils.langchain import convertPdfToJson

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


@app.get('/save_file_in_vector_db')
async def saveFileInVectorDB():
    file_data=convertPdfToJson('https://utfs.io/f/b59b4a54-3673-432d-8667-043a0694b0e3-6na4fi.pdf');
    return {'data':file_data, 'message' : 'File Saved Successfully', 'status' : 200 }




@app.post('/handle_message_response')
async def handleMessageResponse():
    return {'message' : 'Message Response Handled Successfully', 'status' : 200 }   