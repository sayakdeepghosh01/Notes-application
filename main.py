#This is a testing file you can check but don't take it seriously

from typing import Union 

from fastapi import FastAPI

from pydantic import BaseModel #pydentic use for data validation 

app = FastAPI()

class Item(BaseModel):
    name: str
    price_pro: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "Deep"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


