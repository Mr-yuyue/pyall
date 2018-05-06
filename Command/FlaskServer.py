# -*- coding: utf-8 -*-

from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

# set the secret key.  keep this really secret:
app.secret_key = 'HSUkai81;;a!?}{]/8^&(^'

# 根路径
@app.route("/")
def index():
    return "wait"


@app.route("/main")
def main():
    return render_template('Pages/main.html')
    # return "1111"

if __name__ == '__main__':
    # Flask.debug = 1  # 调试模式.
    app.run()

# 再mac下修改1