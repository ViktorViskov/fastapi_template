# libs
from os.path import isfile
from unicodedata import name
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from core.router import ROUTER

# 
# configs
# 

path_to_config = "secret.conf" # path to config file
if (isfile(path_to_config)):
    # create dict from file
    secret = dict(map(lambda line: line.replace("\n","").split("="),open(path_to_config,"r").readlines()))
    pass
else:
    pass
    # default confgis


# class for present this web server
class WEB_SERVER(FastAPI):

    # constructor
    def __init__(self):

        # use super constuctor
        super().__init__()

        # enable CORS
        self.CORS()

        # create routs
        ROUTER(self)

        # static files
        self.STATIC("/")

    # method for allow CORS
    def CORS(self):
        self.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"])

    # method for create static files
    def STATIC(self, url:str = "/", path_to_folder:str = "core/static", mount_name = "static"):
        self.mount(url, StaticFiles(directory=path_to_folder), name=mount_name)


