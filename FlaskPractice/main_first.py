from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

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
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")
        
@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</usr>"

if __name__ == "__main__":
    app.run(debug=True)