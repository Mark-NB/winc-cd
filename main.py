from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", pagename="WINC Continous Deployment Assignment")


@app.route("/home")
def home():
    return redirect("http://188.166.40.219/")


@app.route("/contact")
def contact():
    return render_template("contact.html", pagename="Contact")
