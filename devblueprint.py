#!/usr/bin/python
from datetime import datetime
from flask import Blueprint, jsonify, render_template, request, send_from_directory
import os

# Define the Blueprint for Flask
routes = Blueprint("routes", __name__)

# Inject the "now" variable
@routes.context_processor
def inject_now():
    return {"now": datetime.utcnow()}

# GET: "/"
@routes.route("/")
def Main():
    return render_template("index.html")

# GET: "/relay"
@routes.route("/relay")
def gpio():
    return render_template("relay.html")


def ShutdownServer():
    func = request.environ.get("werkzeug.server.shutdown")
    if func is None:
        raise RuntimeError("Not running with the Werkzeug Server")
    func()
