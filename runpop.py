import os
from flask import Flask, render_template
from flask_pymongo import PyMongo


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')


if __name__ == '__main__':
    app.run(
        host=os.getenv('IP','0.0.0.0'),
        port=int(os.getenv('PORT', '5000')),
        debug=True
    )