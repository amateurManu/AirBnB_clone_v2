#!/usr/bin/python3
""" Script that starts a Flask web application """


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Displays a message """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Displays a message """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text():
    """ Displays 'C' followed by text variable
        Underscore symbols are replaced with a space
    """
    return "C %s" % text.replace('_', ' ')


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text='is cool'):
    """ Displays 'Python' followed by value of <text> """
    if text != 'is cool':
        text = text.replace('_', ' ')
    return "Python %s" % text


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Displays a number n, if it is an integer """
    return "%d is a number" % n


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ Displays an even or odd number """
    return render_template('6-number_odd_or_even.html', number=n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Displays a number """
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
