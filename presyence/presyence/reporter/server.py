from .access_static import get_website_files
from .inject_json_into_js import inject_payload
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse, Response


def run_server_and_inject_payload(payload):
    static_files = get_website_files()
    static_files = { f.route : f for f in static_files }

    index_file = static_files.pop("/index.html")

    worker_route = [k for k in static_files.keys() if k.startswith("/assets/worker")][0]
    worker_file = static_files[worker_route]

    worker_file.content = inject_payload(worker_file.content, payload)

    async def catch_all(request, exc):
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
            return Response(static_file.content, media_type=mime_type)

    for each in static_files.values():
        make_route(each)

    uvicorn.run(app, port=5000, log_level="info")
