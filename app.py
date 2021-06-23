import os
import json
import pandas as pd
import psycopg2
from datetime import datetime
from flask import Flask, abort, request, render_template

app = Flask(__name__)
DATABASE_URL = os.environ.get("DATABASE_URL")

@app.route("/home") #根目錄
def test():
    return render_template("cover.html")

@app.route("/forms", methods=['GET']) #根目錄
def forms():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    sql = "select * from account;"
    dat = pd.read_sql_query(sql, conn)
    conn = None
    table = zip(dat["user_id"], dat["username"])
    return render_template("forms.html", table=table)

@app.route("/sendresult", methods=["POST"])
def sendresult():
    UID = request.form.get("UID")
    content = request.form.get("content")
    try:
        line_bot_api.push_message(UID, TextSendMessage(text=content))
        return render_template("success.html")
    except:
        return render_template("fail.html")
