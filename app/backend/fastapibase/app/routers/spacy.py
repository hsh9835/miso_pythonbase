from fastapi import APIRouter
from pydantic.main import BaseModel

from app.api.spacy.english import *

# /spacy
router = APIRouter()

class Data(BaseModel):
    name: str


@router.post('/test')
def test():
    return {"message": "Welcome to miso."}

@router.post('/test2')
def test2(data: Data):
    print(data)
    return "Success good job SeHwa."


@router.post('/NASAmeme')
def NASAmeme():
    return example1()

@router.post('/spaghetto')
def spaghetto():
    return example2()
