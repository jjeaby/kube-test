import requests
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
def call_svc(svc_name: str, port: int, message: str):
    url = f"http://{svc_name}:{port}/echo/{message}"
    print(url)
    r = requests.get(url)
    print(r.json())
    return r.json()


@app.get("/call-pod/{url}/{message}")
def call_pod(url: str, message: str):
    url = f"http://{url}/echo/{message}"
    print(url)
    r = requests.get(url)
    print(r.json())
    return r.json()

# if __name__ == '__main__':
#     uvicorn.run("main:app", host="0.0.0.0")
