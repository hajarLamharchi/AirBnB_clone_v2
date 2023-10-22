#!/usr/bin/python3
"""This file the / route"""

from flask import Flask, abort, render_template
from models import storage
from models.state import State


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


@app.route('/number_template/<n>', strict_slashes=False)
def template(n):
    """displays an htmml page"""
    if n.isdigit():
        return render_template('5-number.html', n=n)
    else:
        abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def even_odd(n):
    """checks if a number is even or odd"""
    if n.isdigit():
        return render_template('6-number_odd_or_even.html', n=int(n))
    else:
        abort(404)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """displays an HTML page"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """displays an HTML page"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """displays an HTML page"""
    states = storage.all(State)
    if id is not None:
        for state in states.values():
            if state.id == id:
                return render_template('9-states.html', states=states, id=id)
            return render_template('9-states.html', states=None, id=id)
    return render_template('9-states.html', states=states, id=None)


@app.teardown_appcontext
def teardown(exception):
    """remove current session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
