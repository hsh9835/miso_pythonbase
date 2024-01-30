import requests
from fastapi import APIRouter, Request
from fastapi.responses import FileResponse

from app.api.spacy.english import example1
from main import templates

router = APIRouter()

@router.get('/page')
def page():
    return FileResponse('templates/page.html')

@router.get('/flaskget')
def flaskGet():

    remote_server_url = "http://localhost:5000/test/axios/axiosTest"

    response = requests.post(remote_server_url)

    # 응답 처리
    if response.status_code == 200:
        # 성공적인 경우 JSON 응답 반환
        print(response.json())
    else:
        # 실패한 경우 오류 메시지 반환
        print("Failed to send data")


    return FileResponse('templates/page.html')

@router.get('/jinja')
def jinja(request: Request):
    context = {"request": request, "ex1": example1()}
    return templates.TemplateResponse("page.html", context)