from typing import List, Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/api/{item_id}")
def read_item(item_id: str, q: Union[str, None] = None):
  ret = f"""API: {item_id}
mock_response:
  - This is a line of mock API response text.
  - This is a line of mock API response text.
  - This is a line of mock API response text.
  - This is a line of mock API response text.
  - This is a line of mock API response text.
  - This is a line of mock API response text.
test1:
  test2: hello world!
  """
  return ret


class Item(BaseModel):
  items: List[str]

@app.post("/api/batch")
def batch_read_item(item: Item):
  ret = f"""API: {item}
mock_response:
  - This is a line of mock API response text.
  - This is a line of mock API response text.
  - This is a line of mock API response text.
  - This is a line of mock API response text.
  - This is a line of mock API response text.
  - This is a line of mock API response text.
test1:
  test2: hello world!
  """
  return ret