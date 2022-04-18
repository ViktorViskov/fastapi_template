# libs
from fastapi import Request
from fastapi.responses import *

# app components
from app.core.db import Mysql_Connect

# function with logick for main page
def main_page_controller(req: Request):
    # variables
    a = 1

    # modules
    db = Mysql_Connect()
    
    # page logick
    # some logick here

    # create and return response
    return db.Fetch_All("Select * from test;")