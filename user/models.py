from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
# import db database
from app import db
import uuid 

# class
class User:

    # session 
    def start_session(self,user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    # method
    def signup(self):

        # Create the user object
        # object to represent user
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        # Encrypt the password with passlib
        user['password'] = pbkdf2_sha256.encrypt(user['password'])


        # logic to handle "no repeat user email"
        # Check for existing email address
        if db.users.find_one({ "email":user['email'] }):
            return jsonify({"error":"Email address already in use"}), 400




        # set collection within database db
        if db.users.insert_one(user):
            return self.start_session(user)


        return jsonify({"error": "Signup failed"}), 500
    
    
    # singout
    def signout(self):
        session.clear()
        return redirect('/')
    

    # login 
    def login(self):

        # find a user with matching email
        user = db.users.find_one({
            "email": request.form.get('email')
        })

        # if we find one check password, --> start a new session --> return to frontend 
        if user and pbkdf2_sha256.verify(request.form.get('password'),user['password']):
            return self.start_session(user)
        
        # check password 

        # if not able to find one, --> return error

        return jsonify({"error": "Invalid Login Credentials"}), 401 #unauthorised