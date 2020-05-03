from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    title = "Steve Hepples Blog"
    return render_template("index.html", title=title)


@app.route('/about')
def about():
    title = "About Steve Hepple"
    names = ["john", "mary", "wes", "sally"]
    return render_template("about.html", names=names, title=title)

@app.route('/subscribe')
def subscribe():
    title = "Subscribe To Our NewsLetter"
    return render_template("subscribe.html", title=title)
#the code below, note the methods=post...that is because we are posting this to a form.
@app.route('/form', methods=["POST"])
def form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    title = "Thank you, Kindly..."
    return render_template("form.html", title=title, first_name=first_name, last_name=last_name, email=email)
