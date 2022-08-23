import typer
from .discovery import discovery
from .server import run_server
from .access_static import get_website_files
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse, Response

app = typer.Typer()

@app.command()
def run():
    """
    Shoot the portal gun
    """
    typer.echo("running tests...")
    # discovery()
    # run_server()
    static_files = get_website_files()
    static_files = { f.route : f for f in static_files }

    index_file = static_files.pop("/index.html")

#    favicon_file = static_files.pop("/favicon.ico")
#    worker_route = [k for k in static_files.keys() if k.startswith("/assets/worker")][0]
#    worker_file = static_files.pop(worker_route)

    async def catch_all(request, exc):
        print("hit")
        return HTMLResponse(index_file.content, status_code=200)

    exceptions = {
        404: catch_all,
    }

    app = FastAPI(exception_handlers=exceptions)

    @app.get("/")
    def home():
        return HTMLResponse(index_file.content, status_code=200)

    def make_route(static_file):
        extension = static_file.route.split('.')[-1]
        common_media_types = {
            "js" : "application/javascript",
            "ico" : "image/x-icon",
        }
        mime_type = common_media_types.get(extension, "text/html")
        @app.get(static_file.route)
        def route():
            print(static_file.route, mime_type)
            return Response(static_file.content, media_type=mime_type)

    for each in static_files.values():
        make_route(each)

    uvicorn.run(app, port=5000, log_level="info")







"""
async def catch_all(request, exc):
    return FileResponse("dist/index.html", status_code=200)


exceptions = {
    404: catch_all,
}

def run_server():

    app = FastAPI(exception_handlers=exceptions)


    app.mount("/", StaticFiles(directory="dist", html=True), name="static")


    uvicorn.run(app, port=5000, log_level="info")
"""
