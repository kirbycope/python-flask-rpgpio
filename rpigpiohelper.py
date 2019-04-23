#!/usr/bin/python
import RPi.GPIO as GPIO
import time

PinList = [10, 9, 11, 5, 6, 13, 19, 26, 24, 25, 8, 7, 12, 16, 20, 21]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def Cleanup():
    GPIO.cleanup()


def GetState(pinNumber):
    state = 0
    try:
        state = GPIO.input(pinNumber)
    except RuntimeError as ex:
        state = str(ex)
    return state


def GetStates(pinList):
    jsonObject = []
    for pinNumber in pinList:
        state = GetState(pinNumber)
        jsonObject.append({"pinNumber": pinNumber, "state": state})
    return jsonObject


def PulsePin(pinNumber, sleepSeconds=.2):
    jsonObject = []
    state = TurnOnPin(pinNumber, sleepSeconds)
    state = TurnOffPin(pinNumber, sleepSeconds)
    jsonObject.append({"pinNumber": pinNumber, "state": state})
    return jsonObject


def SetupPinAsOutput(pinNumber):
    GPIO.setup(pinNumber, GPIO.OUT)
    return GetState(pinNumber)


def SetupPinsAsOutput(pinList):
    jsonObject = []
    for pinNumber in pinList:
        state = SetupPinAsOutput(pinNumber)
        jsonObject.append({"pinNumber": pinNumber, "state": state})
    return jsonObject


def TogglePin(pinNumber, sleepSeconds=.2):
    state = GetState(pinNumber)
    if (state == 0):
        state = TurnOnPin(pinNumber, sleepSeconds)
    else:
        state = TurnOffPin(pinNumber, sleepSeconds)
    return state


def TogglePins(pinList, sleepSeconds=0):
    jsonObject = []
    for pinNumber in pinList:
        state = TogglePin(pinNumber, sleepSeconds)
        jsonObject.append({"pinNumber": pinNumber, "state": state})
    return jsonObject


def TurnOffPin(pinNumber, sleepSeconds=0):
    GPIO.output(pinNumber, GPIO.LOW)
    time.sleep(sleepSeconds)
    return GetState(pinNumber)


def TurnOffPins(pinList, sleepSeconds=0):
    jsonObject = []
    for pinNumber in pinList:
        state = TurnOffPin(pinNumber, sleepSeconds)
        jsonObject.append({"pinNumber": pinNumber, "state": state})
    return jsonObject


def TurnOnPin(pinNumber, sleepSeconds=0):
    GPIO.output(pinNumber, GPIO.HIGH)
    time.sleep(sleepSeconds)
    return GetState(pinNumber)


def TurnOnPins(pinList, sleepSeconds=0):
    jsonObject = []
    for pinNumber in pinList:
        state = TurnOnPin(pinNumber, sleepSeconds)
        jsonObject.append({"pinNumber": pinNumber, "state": state})
    return jsonObject
