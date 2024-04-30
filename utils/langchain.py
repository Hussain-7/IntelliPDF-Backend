
from langchain_community.document_loaders import PyPDFLoader
import uuid
import requests
import logging
import os

def convertPdfToJson(fileLink):
		response = requests.get(fileLink)
		logging.info(f"response: {response}")
		fileId = uuid.uuid4()
		filename= f'{fileId}-temp.pdf'
		logging.info(f"filename: {filename}")
		with open(filename, 'wb') as f:
			f.write(response.content)
    
    # Parse the pdf to pages to text 
		loader = PyPDFLoader(filename)
		pageLevelDocs = loader.load()
		# delete the file with the filename
		os.remove(filename)
		return pageLevelDocs