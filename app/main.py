# ASGI-Asynchronous Server gateway Interface
#WSGI-Webserver Gateway Interface
from fastapi import FastAPI
from pydantic import BaseModel
from app.routes.health import router
import uvicorn

port=8000
app=FastAPI()

class base(BaseModel):
    text:str

@app.get("/")
def message() -> str:
    return f"Fast API is running at {port}"

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=port, reload=True)
    # FAstAPI runs of port 8000