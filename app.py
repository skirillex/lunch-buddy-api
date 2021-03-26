from flask import Flask
app = Flask(__name__)

base_route = '/api/v1/'

@app.route(base_route)
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
