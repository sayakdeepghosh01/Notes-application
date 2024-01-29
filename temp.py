from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Union

from pymongo import MongoClient



app = FastAPI()

app.mount("/static", StaticFiles(directory = "static"), name = "static")
templates = Jinja2Templates(directory = "templates")

conn = MongoClient("mongodb+srv://sayak-0012:1234@sayakghosh.lhh4cof.mongodb.net") #mongodb instense




# @app.get("/")
# def read_root():
#     return {"Temp": "Use in FAPI"}

@app.get("/", response_class = HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
#i store the notes from mongodb database to docs, for one docs access i can write- find_one({}) othwrwise i have to use  a forloop
    # for docs in docs:
    #     print(docs) #print the docs so that the files can print in my terminal. this loop print all files from MOngoDB
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "note": doc["note"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})

@app.get("/items/{item_id}")
def read_root(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}










