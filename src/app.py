from flask import Flask

app=Flask(__name__)


@app.route("/")
def sayHello():
    return f'Hello World !!!'


if __name__ == "__main__" :
    app.run(port=4000,host="0.0.0.0")
    