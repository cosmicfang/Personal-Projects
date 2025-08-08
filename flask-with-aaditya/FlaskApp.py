from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/user/<name>/")     #---------This will grab the value of name from URL and the n pass it as a parameter to the Function--------->
def user(name):
    return f"Hello {name} !!!"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Administrator SAAABB!"))   #---------Can be used to redirect to another page if necessary--------->


if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 8080
    app.run(host=HOST, port=PORT)