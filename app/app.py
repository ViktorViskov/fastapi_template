# libs
from fastapi import FastAPI
from app.core.router import ROUTER
from app.core.middleware import MIDDLEWARE
from app.core.cors import CORS
from app.core.static import STATIC

# 
# configs
# 

# class for present this web server
class WEB_SERVER(FastAPI):

    # constructor
    def __init__(self):

        # use super constuctor
        super().__init__()

        # enable CORS
        CORS(self)

        # enable middleware
        MIDDLEWARE(self)

        # enable routing
        ROUTER(self)

        # enable static files
        STATIC(self)