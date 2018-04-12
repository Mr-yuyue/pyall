from flask import Flask,redirect

app = Flask(__name__)

# set the secret key.  keep this really secret:
app.secret_key = 'HSUkai81;;a!?}{]/8^&(^'

# 根路径
@app.route('/')
def index():
    return "wait"

@app.route("/main")
def main():
    return ""

if __name__ == '__main__':
    app.run()
