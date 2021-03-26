from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient("localhost", 27017)
db = client.get_jason_database('total_records')
records = db.register
meetings = db.meeting


@app.route("/")
def login():
    email = request.get_jason("email")
    user = request.get_jason("user")
    # email_found = records.find_one({"email": email})
    user_input = {'name': user, 'email': email, 'confirmation':False}
    records.insert_one(user_input)
    return jsonify(user_input)

@app.route("/confirmation")
def confirmation():
    email = request.get_jason("email")
    confirmation = request.get_jason("input")
    if confirmation:
        records.update_one({'email': email}, {'confirmation': True})

@app.route("/launchmeeting")
def launchmeeting():
    email = request.get_jason("email")
    launchmeetinginput = request.get_jason("launchmeetinginput")
    if launchmeetinginput:
        meetingid = "https://daily-harvest.zoom.us/j/92117162158?pwd=TEZQYXo1NGM0Nk5yNWl2TVVsdGZyZz09"
        meeting = {'meetingid': meetingid }
        meetings.insert_one(meeting)
        const_query = {'confirmation':True}
        const_projection = {'email':1, 'name':1}
        second_user= records.find_one (const_query,const_projection)
        records.update_one ({'email': second_user.email},{'confirmation': False})
        records.update_one({'email': email}, {'confirmation': False})
        return request.query_string


if __name__ == '__main__':
    app.run('0.0.0.0')
