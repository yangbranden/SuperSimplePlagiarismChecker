from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def counter():
    return render_template('counter.html')