#!/usr/bin/python
from datetime import datetime
from flask import Blueprint, jsonify, render_template, request, send_from_directory
import os
import rpigpiohelper as RpiGpioHelper

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
def relay():
    return render_template("relay.html")

# GET: "/pulse/<pinNumber>"
@routes.route("/pulse/<pinNumber>")
def PulsePin(pinNumber):
    jsonObject = RpiGpioHelper.PulsePin(int(pinNumber))
    return jsonify(jsonObject)

# GET: "/setup/<pinNumber>?asType=output>"
@routes.route("/setup/<pinNumber>")
def SetupPin(pinNumber):
    asType = request.args.get("asType")
    if (asType == "output"):
        state = RpiGpioHelper.SetupPinAsOutput(int(pinNumber))
    else:
        state = "The asType '" + asType + "' not implemented"
    return jsonify(state)

# GET: "/setup?asType=output"
@routes.route("/setup")
def SetupPins():
    asType = request.args.get("asType")
    if (asType == "output"):
        state = RpiGpioHelper.SetupPinsAsOutput(RpiGpioHelper.PinList)
    else:
        state = " The asType '" + asType + "' not implemented"
    return jsonify(state)

# GET: "/shutdown"
@routes.route("/shutdown")
def Shutdown():
    ShutdownServer()
    RpiGpioHelper.Cleanup()
    return "Server shutting down..."

# GET: "/states"
@routes.route("/states")
def GetStates():
    jsonObject = RpiGpioHelper.GetStates(RpiGpioHelper.PinList)
    return jsonify(jsonObject)

# GET: "/state/<pinNumber>"
@routes.route("/state/<pinNumber>")
def GetState(pinNumber):
    state = RpiGpioHelper.GetState(int(pinNumber))
    return jsonify({"pinNumber": pinNumber, "state": state})

# GET: "/toggle/<pinNumber>"
@routes.route("/toggle/<pinNumber>")
def TogglePin(pinNumber):
    state = RpiGpioHelper.TogglePin(int(pinNumber))
    return jsonify({"pinNumber": pinNumber, "state": state})

# GET: "/turnoff/<pinNumber>"
@routes.route("/turnoff/<pinNumber>")
def TurnOffPin(pinNumber):
    state = RpiGpioHelper.TurnOffPin(int(pinNumber))
    return jsonify({"pinNumber": pinNumber, "state": state})

# GET: "/turnon/<PinNumber>"
@routes.route("/turnon/<pinNumber>")
def TurnOnPin(pinNumber):
    state = RpiGpioHelper.TurnOnPin(int(pinNumber))
    return jsonify({"pinNumber": pinNumber, "state": state})


def ShutdownServer():
    func = request.environ.get("werkzeug.server.shutdown")
    if func is None:
        raise RuntimeError("Not running with the Werkzeug Server")
    func()
