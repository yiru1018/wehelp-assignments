from flask import (
    Flask, render_template, request, session, redirect, url_for, Blueprint, 
    jsonify, make_response)

import mysql.connector

app=Flask(__name__)
app.secret_key="oppppppooop"

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="oooooooooo",
  database="website"
)

mycursor = mydb.cursor()

@app.route("/")
def index():    
    return render_template("index.html")

@app.route("/member")
def member():
    if "username" in session:
        return render_template("member.html", name=session["name"])
    else:
        return redirect("/")

@app.route("/error")
def error():
    args=request.args.get("message")
    return render_template('error.html', message=args)

@app.route("/signin", methods=["POST"])
def signin():
    username=request.form["username"]
    password=request.form["password"]

    mycursor.execute("SELECT name FROM member WHERE username=%s AND password=%s", (username, password,))
    name = mycursor.fetchone()

    if name:
        session["name"]=name[0]
        session["username"]=username         
        return redirect("/member")
    elif username=="" or password=="":
        return redirect(url_for("error", message="請輸入帳號、密碼"))
    else:
        return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))

@app.route("/signout")
def signout():
    session.pop('username',None)
    return redirect("/")

@app.route("/signup", methods=["POST"])
def signup():
    new_name=request.form["name"]
    new_username=request.form["username"]
    new_password=request.form["password"]

    mycursor.execute("SELECT username FROM member WHERE username=%s", (new_username,))
    username=mycursor.fetchone()
    
    if username:
        return redirect(url_for("error", message="帳號已經被註冊"))
    else:
        mycursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)",
        (new_name, new_username, new_password,))
        mydb.commit()
        return redirect("/")
    

@app.route("/api/members/")
def get_name():
    username=request.args.get("username")
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT id, name, username FROM member WHERE username=%s",(username,))
    member_data=mycursor.fetchone()    
    return make_response(jsonify({"data":member_data}))
    

@app.route("/api/member", methods=["POST"])
def edit_name():
    new_name=request.json.get("name")
    mycursor.execute("UPDATE member SET name=%s WHERE username=%s",(new_name, session["username"]))
    mydb.commit()
    counts=mycursor.rowcount

    if counts==1:
        result={"ok":True}
    else:
        result={"error":True}
    return make_response(jsonify(result))


if __name__ == "__main__":
    app.run(port=3000)

