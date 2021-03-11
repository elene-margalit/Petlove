import flask
import json
from flask import request
from database import db

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.route('/', methods=['GET'])
def home():
    return "<p>Petlove</p>"

@app.route('/api/v1/register', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        data = request.form
        email = data["email"]
        username = data["username"]
        password = data["password"]
        if(db.is_record_present(email, username)):
            response = "Username or email is already taken, sorry"
        else:
            response = db.create_record(email, username, password)
        return "{}".format(response)
    return "<p>Send normal request</p>"


@app.route('/api/v1/delete', methods=['GET', 'POST'])
def delete_account():
    if request.method == 'POST':
        data = request.form
        email = data["email"]
        username = data["username"]
        if(not db.is_record_present(email, username)):
            response = "Username or email does not exist."
        else:
            response = db.delete_record(email, username)
        return "{}".format(response)
    return "<p>Send normal request</p>"


@app.route('/api/v1/update_username', methods=['GET', 'POST'])
def update_username():
    if request.method == 'POST':
        data = request.form
        old_username = data["old_username"]
        new_username = data["new_username"]
        if(not db.is_record_present("", old_username)):
            response = "Username does not exist."
        else:
            response = db.update_username(old_username, new_username)
        return "{}".format(response)
    return "<p>Send normal request</p>"

@app.route('/api/v1/update_email', methods=['GET', 'POST'])
def update_email():
    if request.method == 'POST':
        data = request.form
        old_email = data["old_email"]
        new_email = data["new_email"]
        if(not db.is_record_present(old_email, "")):
            response = "Email does not exist."
        else:
            response = db.update_email(old_email, new_email)
        return "{}".format(response)
    return "<p>Send normal request</p>"

#Needs Improvement
@app.route('/api/v1/update_pass', methods=['GET', 'POST'])
def update_password():
    if request.method == 'POST':
        data = request.form
        old_pass = data["old_pass"]
        new_pass = data["new_pass"]
        response = db.update_pass(old_pass, new_pass)
        return "{}".format(response)
    return "<p>Send normal request</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

app.run()
