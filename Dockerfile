FROM python:latest

RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r ./requirements.txt
COPY main*.py ./
EXPOSE 8000

ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]
