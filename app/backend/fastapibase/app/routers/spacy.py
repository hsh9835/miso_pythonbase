from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.api.spacy.english import *

router = APIRouter() # /spacy


@router.get('/test')
def test():
    return {"message": "Success good job SeHwa."}

@router.post('/test2')
def test2():
    print("test2")
    return JSONResponse(content={"message": "Success good job SeHwa."})


@router.post('/NASAmeme')
def NASAmeme():
    return example1()

@router.post('/spaghetto')
def spaghetto():
    return example2()
