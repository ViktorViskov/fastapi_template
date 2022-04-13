# libs
from fastapi.responses import *
from fastapi import FastAPI



# method for define different routes in web app
def ROUTER(SERVER: FastAPI):

    # main page route
    @SERVER.get("/", response_class=HTMLResponse)
    async def main_page():
        return FileResponse("core/static/index.html")

    # main page route
    @SERVER.get("/test")
    async def main_page():
        return HTMLResponse("Hello world!",status_code=200)