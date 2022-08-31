from .access_static import get_website_files, WebsiteStaticFile
from .inject_json_into_js import inject_payload
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse, Response


def run_server_and_inject_payload(payload):
    """Serve the Vue.JS spa and inject it the reports from the test runner.

    1. Gather each file required for the Vue.JS SPA into a dictionary of `WebsiteStaticFile` objects.
    2. Isolate the files with special roles, here : `assets/worker.js` and `index.js`.
    3. For the worker file, inject the payload inside. We will define its route handler in step 6.
    4. For the index file, redirect every URL that doesn't match to it.
    5. Then create the route handler for the `/` route. (returning `index.html`)
    6. Then for every static file, create a FastAPI route handler that returns the file alongside the correct MIME type.
    7. Then serve the app.
    """
    static_files = get_website_files()
    static_files = {
        f.route: f for f in static_files
    }  # index the static file by their route for easier handling

    # because of the bundling process, the name of the is not exactly `/assets/worker.js`
    worker_route = [k for k in static_files.keys() if k.startswith("/assets/worker")][0]
    worker_file = static_files[worker_route]

    worker_file.content = inject_payload(worker_file.content, payload)

    # we override 404 to redirect to the index.html (which is the SPA entrypoint).
    # the reason is the SPA uses its own router client-side which doesnt match the static files.
    index_file = static_files.pop("/index.html")

    async def catch_all(request, exc):
        return HTMLResponse(index_file.content, status_code=200)

    exceptions = {
        404: catch_all,
    }

    app = FastAPI(exception_handlers=exceptions)

    # define the routes
    @app.get("/")
    def home():
        return HTMLResponse(index_file.content, status_code=200)

    # route factory
    def make_route(static_file: WebsiteStaticFile):
        """Makes FastAPI route from a WebsiteStaticFile object"""
        extension = static_file.route.split(".")[-1]
        common_media_types = {
            "js": "application/javascript",
            "ico": "image/x-icon",
            "css": "text/css",
            "html": "text/html",
        }
        mime_type = common_media_types.get(extension)
        if not mime_type:
            raise NotImplementedError

        @app.get(static_file.route)
        def route():
            return Response(static_file.content, media_type=mime_type)

    for each in static_files.values():
        make_route(each)

    uvicorn.run(app, port=5000, log_level="info")
