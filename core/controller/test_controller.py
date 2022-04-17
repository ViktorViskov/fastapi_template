# libs
from random import randint
from core.middleware.db import Mysql_Connect

# function controller for page test
def test_controller():
    random_num = randint(1,10000)
    db = Mysql_Connect("10.0.0.2", "root", "dbnmjr031193", "template_test")

    html_page = open("./core/view/test.html").read()
    html_page = html_page.replace("!!!RANDOM!!!",  str(random_num))

    # add record to db
    db.Exec("insert into test (name) values (%s)", True, random_num)
    

    html_page = html_page.replace("!!!DB!!!",  str(db.Exec("Select * from test;")))
    return html_page