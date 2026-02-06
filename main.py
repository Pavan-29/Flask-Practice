from flask import Flask

app = Flask(__name__)  #__name__ = main.py

@app.route("/")  #endpoint, when user visits "/" this function will be executedfla
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ping", methods=["GET","POST"])
def ping():
    return "why are you pinging me?"


if __name__ == "__main__":
    app.run(debug=True)