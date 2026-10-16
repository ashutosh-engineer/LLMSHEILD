# ASGI-Asynchronous Server gateway Interface
#WSGI-Webserver Gateway Interface
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

port=8000
app=FastAPI()

class base(BaseModel):
    text:str


@app.get("/health")
def check_health():
    return {"status" : "Healthy -Server is running"}

@app.get("/message")
def message() -> str:
    return f"Fast API is running at {port}"

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)
    # FAstAPI runs of port 8000