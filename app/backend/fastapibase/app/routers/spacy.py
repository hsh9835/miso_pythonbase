from fastapi import APIRouter

from ..api.spacy.english import *

router = APIRouter()


@router.get('/test')
def test():
    return {"message": "Success good job SeHwa."}


@router.post('/NASAmeme')
def NASAmeme():
    return example1()


@router.post('/spaghetto')
def spaghetto():
    return example2()
