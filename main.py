from typing import List
from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()


@app.get('/test')
def test_view():
    return {
        "IsReport":"Success",
        "Msg": "It is working"
    }

@app.get('/')
def doc_view():
    return RedirectResponse(url="/docs/")