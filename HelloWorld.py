from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "<p>Hello, World!</p>"

@app.route("/page2")
def page2():
    return "I am now on page 2!"