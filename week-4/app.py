from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import url_for



app=Flask(__name__)
app.secret_key="oppppppooop"

@app.route("/")
def index():    
    return render_template("index.html")

@app.route("/member")
def member():
    if session["signin"]==True:
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error")
def error():
    args=request.args.get("message")
    return render_template('error.html', message=args)

@app.route("/signin" ,methods=["POST"])
def signin():
    account=request.form["account"]
    password=request.form["password"]


    if account=="test" and password=="test":
        session["signin"]=True
        return redirect("/member")
    elif account=="" or password=="":
        return redirect(url_for("error", message="請輸入帳號、密碼"))
    else:
        return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))

@app.route("/signout")
def signout():
    session["signin"]=False
    return redirect("/")
app.run(port=3000)
