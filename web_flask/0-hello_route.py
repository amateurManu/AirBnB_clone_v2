#!/usr/bin/python3
""" This module serves a script for starting a live web server """


from flask import Flask

app = Flask(__name__)
""" Instatiating the Flask class """


@app.route("/", strict_slashes=False)
def hello_route():
    """ Prints a message """
    return "<p>Hello HBNB!<p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
