from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "!@#$%qwerty"
app.permanent_session_lifetime = timedelta(days=5)


@app.route("/")
def home():
    page = render_template("index.html")
    return page

@app.route("/test")
def test():
    page = render_template("navbar.html")
    return page

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login Successfull!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("login"))

        return render_template("login.html")
        
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("You are noit logged in")
        return redirect(url_for("login"))
    

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have logged out successfully, {user}", "info")
    session.pop("user", None)
    return redirect(url_for("login"))
    
    
if __name__ == "__main__":
    app.run(debug=True)