from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        return "signup succsess"
    
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    else:
        if bob == request.form["username"] and \
           123 == request.form["password"]:
            return "Hello " + request.form
        else:
            return "wrong password"

