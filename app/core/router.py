# libs
from fastapi.responses import *
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# import page controllers
from app.controller.main_page_controller import main_page_controller
from app.controller.test_controller import test_controller

# method for define different routes in web app
def ROUTER(SERVER: FastAPI):

    # jinja2 templates module
    templates = Jinja2Templates(directory="app/view")

    # main page route
    @SERVER.get("/", response_class=HTMLResponse)
    async def main_page( req: Request):
        # data from controller
        obj = main_page_controller(req)
        return templates.TemplateResponse("main.jinja", {"request": req, "obj": obj})

    # test
    @SERVER.get("/test")
    async def test(req: Request):
        # data from controller
        obj = test_controller(req)
        return templates.TemplateResponse("test.jinja", {"request": req, "obj": obj})