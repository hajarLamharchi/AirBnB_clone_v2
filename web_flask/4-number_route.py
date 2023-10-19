#!/usr/bin/python3
"""This file the / route"""

from flask import Flask, abort

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays hello hbnb!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """displays c + text"""
    return "C " + str(text).replace('_', ' ')


@app.route('/python', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_is_cool(text):
    """displays python + text"""
    return "Python " + str(text).replace('_', ' ')


@app.route('/number/<n>', strict_slashes=False)
def is_number(n):
    """checks if n is number"""
    if n.isdigit():
        return "{} is a number".format(n)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
