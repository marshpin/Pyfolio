from flask import Flask

app = Flask("Pyfolio")


@app.route('/')
def hello_world():
    return "Flask Test"