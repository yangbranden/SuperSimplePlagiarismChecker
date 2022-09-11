from flask import Flask, render_template, request
from difflib import SequenceMatcher

app = Flask(__name__)

@app.get("/")
def form_get():
    return render_template('input.html')

@app.post("/output.html")
def form_post():
    left_text = request.form.get('left_box')
    right_text = request.form.get('right_box')
    print(left_text, right_text)

    # now we can use python code to change our HTTP GET request data
    similarity = SequenceMatcher(None, left_text, right_text).ratio() # get the similarity ratio between the two strings
    similarity = round(similarity, 4) # restrict our number to 2 decimals
    similarity_percent = str(similarity * 100) + "%" # format it as a percent (rather than a decimal)

    return render_template('output.html', left_output=left_text, right_output=right_text, similarity_output=similarity_percent)