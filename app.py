import os
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/experience", methods=["GET"])
def experience():
    """Show experience"""
    return render_template("experience.html")


@app.route("/misc", methods=["GET"])
def misc():
    """Show misc"""
    return render_template("misc.html")


@app.route("/education", methods=["GET"])
def education():
    """Show education"""
    return render_template("education.html")

# projects?
