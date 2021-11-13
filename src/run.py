# -*- coding:utf-8-*-
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()


class CityInfo(BaseModel):
    province: str
    country: str
    is_affected: Optional[bool] = None


@app.get('/')
def hello_world():
    return {'Hello': 'FastAPI'}


@app.get('/city/{city}')
def result(city: str, query_string: Optional[str] = None):
    return {'city': city, 'query_string': query_string}


@app.put('/city/{city}')
def result(city: str, city_info: CityInfo):
    return {'city': city, 'country': city_info.country, 'is_affected': city_info.inferred}


if __name__ == '__main__':
    # 执行命令启动 : uvicorn run:app --reload
    # uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True, debug=True, workers=4)  # worker:进程的数量
    uvicorn.run('run:app', host='127.0.0.1', port=8000, reload=True)
