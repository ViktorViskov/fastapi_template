# libs
from os.path import isfile
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

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


# web server
web_server = FastAPI()


# 
# CORS
# 

web_server.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 
# static files
# 

web_server.mount("/static", StaticFiles(directory="static"), name="static")


# 
# Routes
# 

# VUE js app
@web_server.get("/")
async def main_page():
    return HTMLResponse("Hello world!",status_code=200)
