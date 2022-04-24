# libs
from fastapi.responses import *
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# import page controllers
from app.controller import c_main
from app.controller import c_test

# method for define different routes in web app
def ROUTER(SERVER: FastAPI):

    # jinja2 templates module
    templates = Jinja2Templates(directory="app/view")

    # main page route
    @SERVER.get("/", response_class=HTMLResponse)
    async def processor( req: Request):
        # data from controller
        obj = c_main.controller(req)
        return templates.TemplateResponse("main.jinja", {"request": req, "obj": obj})

    # test
    @SERVER.get("/test")
    async def processor(req: Request):
        # data from controller
        obj = c_test.controller(req)
        return templates.TemplateResponse("test.jinja", {"request": req, "obj": obj})