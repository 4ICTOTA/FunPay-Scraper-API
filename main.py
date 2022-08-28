from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from apps.routes import router as api


app = FastAPI(
    title = "FunPay parser API")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],)

app.include_router(
    router = api)


@app.get("/")
async def main():
    return RedirectResponse(
        url = "/docs/")