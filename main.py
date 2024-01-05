# 啟動 API 指令
# uvicorn main:app --reload
import json
from toolkit.sqloperate import SqlOperate
from fastapi import FastAPI
from typing import Optional


app = FastAPI()  # 建立一個 Fast API application


@app.get("/")  # 指定 api 路徑 (get方法)
async def root():
    return {"message": "Hi!"}


# @app.get("/items/{item_id}")  # 指定 api 路徑 (get方法)
# async def read_item(item_id: int, q: Optional[str] = None):

#     return {"item_id": item_id, "q": q}


# @app.get("/quote/symbol={symbol}")  # 指定 api 路徑 (get方法)
# async def get_quote(symbol: int, start: int, end: int):
#     return {"symbol": symbol, "start date": start, "end date": end}

# @app.get("/test")  # 指定 api 路徑 (get方法)
# async def test():
#     return {"message": "Hi!"}


@app.get("/test")  # 指定 api 路徑 (get方法)
async def get_quote(start: int, end: int):
    syntax = """
        SELECT *
        FROM excercise
        WHERE excercise."Id" BETWEEN :from AND :end 
    """
    syntax_params = {
        'from': start,
        'end': end,
    }
    sql_operate = SqlOperate()
    data = sql_operate.pg_api_query(syntax, syntax_params)
    return data
