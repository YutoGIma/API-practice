from typing import Optional
import sqlite3
from fastapi import FastAPI
from fastapi.params import Query,Body
import google_books

app = FastAPI()
DATABASE_URL="./fastapi_sample.db"

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = Query(None) , b:str=Body(None)):
    return {"item_id": item_id, "q": q , "b" : b}

@app.get("/books/{isbn}")
def books(isbn:str):
    book=google_books.get(isbn)
    return {"book":book}

@app.get("/books")
def get_books():
    connect=sqlite3.connect(DATABASE_URL)
    c=connect.cursor()
    c.execute("select * from books")
    books = c.fetchall()
    result=[]
    for book in books:
        result.append(
            dict(
                id=book[0],
                title=book[1],
                authors=book[2],
                publishData=book[3],
                description=book[4],
                image=book[5],
                stock=book[6],
            )
        )
    c.close()
    connect.close()
    return dict(result=result)
