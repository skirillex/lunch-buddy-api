from flask import Flask
from pymongo import MongoClient

client = MongoClient(host="localhost", port=27017)
db = client["lunch-buddy"]
user = db.user

app = Flask(__name__)

base_route = '/api/v1/'

@app.route(base_route)
def hello():
    return "hello world"

@app.route(base_route+'test')
def test():
    for x in user.find():
        return x

if __name__ == '__main__':
    app.run(host='0.0.0.0')
