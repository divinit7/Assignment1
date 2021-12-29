import pickle

import flask
from flask import Flask, jsonify, render_template, request

from fetchjson1 import jsonTohtml

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
