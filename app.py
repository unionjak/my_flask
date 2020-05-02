from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    title = "Steve Hepples Blog"
    return render_template("index.html", title=title)


@app.route('/about')
def about():
    names = ["john", "mary", "wes", "sally"]
    return render_template("about.html", names=names)
