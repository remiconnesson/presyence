import uvicorn

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

async def catch_all(request, exc):
    return FileResponse("dist/index.html", status_code=200)


exceptions = {
    404: catch_all,
}

app = FastAPI(exception_handlers=exceptions)


app.mount("/", StaticFiles(directory="dist", html=True), name="static")


uvicorn.run(app, port=5000, log_level="info")
