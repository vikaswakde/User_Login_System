from flask import Flask, render_template, session, redirect
from functools import wraps

app = Flask(__name__)
app.secret_key = b'\x1f\x98\xdb\xc3;\xe9)7@\x8a\x88^\x976"\x1d'


# Database
from pymongo import MongoClient

# Enter your MongoClient------ <password> ---- 
client = MongoClient(
    "mongodb+srv://vikaswakdepc:<password>@cluster0.89a4blc.mongodb.net/?retryWrites=true&w=majority"
)

db = client.user_login_system_2


# Decorators


# Defining a decorator function named 'login_required'
def login_required(f):
    # Using wraps decorator to preserve the metadata of the decorated function 'f'
    @wraps(f)
    # Defining a new function 'wrap' that will replace the original function 'f'
    def wrap(*args, **kwargs):
        # Checking if the key 'logged_in' exists in the session dictionary
        if "logged_in" in session:
            # If 'logged_in' is in the session, call the original function 'f' with its arguments and return its result
            return f(*args, **kwargs)
        else:
            # If 'logged_in' is not in the session (i.e., the user is not logged in), redirect the user to the home page
            return redirect("/")

    # Returning the new function 'wrap'. Now, whenever the decorated function is called, it will actually call 'wrap' instead
    return wrap


# tell app.py about "routes.py"
# Routes
# from "user" -> folder import "routes.py"
from user import routes


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/dashboard/")
@login_required
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
