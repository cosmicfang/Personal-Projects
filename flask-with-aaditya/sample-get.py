from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
# Since session data is encrypted, we need a secret key to use it
app.secret_key = "abcde123"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))


if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 8080
    app.run(host=HOST, port=PORT)