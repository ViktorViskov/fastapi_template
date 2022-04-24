# libs
from random import randint
from fastapi import Request
from fastapi.responses import *

# app components
from app.core.db import Mysql_Connect

# function controller for page test
def controller(req: Request):
    # variables
    random_num = randint(1,10000)

    # modules
    # db = Mysql_Connect()

    # page logick
    # some logick here

    # create and return response
    # return {"random": random_num, "numbers": db.Fetch_All("Select * from test;")}
    return {"random": random_num, "numbers": [1,2,3,4,5]}