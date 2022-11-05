FROM python:latest

RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r ./requirements.txt
COPY main*.py ./
EXPOSE 8080 8081
WORKDIR /

ENTRYPOINT [ "sh" ]
#CMD [  '-m', 'uvicorn', 'app.main:app',  '--port=8080', '--host="0.0.0.0"' ]
#CMD [ "main.py" ]
