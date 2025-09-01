from fastapi import FastAPI
# from app.interface.routers import user_router
from app.api import autenticacao

app = FastAPI()

app.include_router(autenticacao.router)
