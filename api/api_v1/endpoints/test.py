from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

import crud, models, schemas
from api import deps
from core.config import settings
from utils import send_new_account_email
from starlette.responses import RedirectResponse

router = APIRouter()


# @router.get("/")
# def docs_view():
#     return RedirectResponse(url="/docs/")

@router.get("/")
def test():
    return{'msg':'sdkfjskdfkl'}
