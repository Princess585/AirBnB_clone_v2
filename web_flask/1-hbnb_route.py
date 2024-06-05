#!/usr/bin/python3
"""A sript that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)
app.url map.strict_slashes = False


@app.route('/')
def home():
    """
Displays 'Hello HBNB!'.
    """
    return 'Hello HBNB!'


@app.route('/hbnb/')
def hbnb():
    """

    """
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

