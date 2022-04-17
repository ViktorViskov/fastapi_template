# libs
from fastapi.responses import *
from fastapi import FastAPI
from core.controller.main_page_controller import main_page_controller
from core.controller.test_controller import test_controller

# method for define different routes in web app
def ROUTER(SERVER: FastAPI):

    # main page route
    @SERVER.get("/", response_class=HTMLResponse)
    async def main_page():
        return HTMLResponse(main_page_controller())

    # main page route
    @SERVER.get("/test")
    async def test():

        return HTMLResponse(test_controller())