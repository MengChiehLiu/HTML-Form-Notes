from flask import Flask, abort, request, render_template
import psycopg2
import pandas as pd
import os
DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a nccuacct-angels').read()[:-1]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('cover.html')

@app.route('/forms', methods=['GET'])
def api_services():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    sql = "select * from account;"
    dat = pd.read_sql_query(sql, conn)
    conn = None
    table = zip(dat["user_id"], dat["username"])
    return render_template('test.html', table=table)

if __name__ =="__main__":
    app.run(debug=True)

