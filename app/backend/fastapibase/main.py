from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.plugins.router_autoset import *

app = FastAPI()
templates = Jinja2Templates(directory="templates")
# 정적 파일 서빙을 위한 디렉토리를 설정
app.mount("/static", StaticFiles(directory="build/static"), name="static")

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],  # React 애플리케이션의 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_routers(app)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/reactest")
async def reactest():
    return FileResponse("build/index.html")
