
docker build -t backend-server -f dockerfile .
docker run -p 4000:4000  -it backend-server

