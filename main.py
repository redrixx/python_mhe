from typing import Union
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from message_parser import *

class DivertMessage(BaseModel):
    OlpnId: str
    DivertLocation: str

class DivertList(BaseModel):
    Data: List[DivertMessage]

class Message(BaseModel):
    message: str

app = FastAPI()

@app.get("/helloworld")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/mhe/createDivertMessages")
def read_divert_list(divertMessages: DivertList):
    response = {}
    for divertMessage in divertMessages.Data:
        response[f"{divertMessage.OlpnId}"] = "Diverted to " + divertMessage.DivertLocation
    return response

@app.get("/mhe/sendMessage")
def respond(message: Message):
    try:
        return parse_message(message.message)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
