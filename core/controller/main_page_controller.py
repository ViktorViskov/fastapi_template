from core.middleware.db import Mysql_Connect

# function with logick for main page
def main_page_controller():
    db = Mysql_Connect("10.0.0.2", "root", "dbnmjr031193", "template_test")

    html_page = open("./core/view/main.html").read()
    html_page = html_page.replace("!!!DATE!!!",  str(db.Exec("Select * from test;")))
    return html_page