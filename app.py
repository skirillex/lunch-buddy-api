from flask import Flask, render_template, request, url_for, redirect, session
from flask_pymongo import PyMongo
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient("localhost", 27017)
db = client.get_database('total_records')
records = db.register


@app.route("/")
def login():
    email = request.form.get("email")
    user = request.form.get("user")
    # email_found = records.find_one({"email": email})
    user_input = {'name': user, 'email': email, 'confirmation':False}
    records.insert_one(user_input)
    return user_input

@app.route("/confirmation")
def confirmation():
    email = request.form.get("email")
    confirmation = request.form.get("input")
    if confirmation:
        records.update_one({'email': email}, {'confirmation': True}),



if __name__ == '__main__':
    app.run('0.0.0.0')
