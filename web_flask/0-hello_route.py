#!/usr/bin/python3
""" Script that starts a web application """

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """ Displays a message """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
