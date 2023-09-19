from flask import Flask
# import "app" instance form app.py
from app import app
# import class "User" from "user" -> directory/folder -> "models" file
from user.models import User

@app.route('/user/signup', methods=['POST'])
def signup():
    # new class instance -> User()
    return User().signup()

@app.route('/user/signout')
def signout():
    # user instance and singout() method
    return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
    # user instance and  login() method   --> that we have deined in "models.py"
    return User().login()