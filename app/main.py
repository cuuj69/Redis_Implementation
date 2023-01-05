from fastapi import FastAPI
from fastapi import APIRouter
import router

app = FastAPI()

@app.get('/')
async def Home():
    return "Welcome Home"


app.include_router(router.router)