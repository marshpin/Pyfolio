from flask import *

app = Flask("Pyfolio")


@app.route('/')
def hello_world():
    return render_template("index.html")