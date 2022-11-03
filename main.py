import requests
import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/echo/{message}")
def echo(message: str, request: Request):
    client_host = request.client.host
    return {"echo": client_host, "message": message}


@app.get("/call-svc/{svc_name}/{port}/{message}")
def call(svc_name: str, port: int, message: str, request: Request):
    url = f"http://{svc_name}:{port}/echo/{message}"
    print(url)
    r = requests.get(url)
    print(r.json())
    return r.json()


@app.get("/call-pod/{pod_name}/{message}")
def call(pod_name: str, message: str, request: Request):
    url = f"http://{pod_name}.default:8000/echo/{message}"
    print(url)
    r = requests.get(url)
    print(r.json())
    return r.json()


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0")
