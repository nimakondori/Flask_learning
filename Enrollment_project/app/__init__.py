from flask import Flask

app = Flask(__name__)
# __name__ is just the current module


@app.route("/")
@app.route("/index")
def index():
    return "<h1>Hello World!</h1>"
