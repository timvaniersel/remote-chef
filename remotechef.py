from flask import Flask, redirect
import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

app = Flask(__name__)
kit = MotorKit(i2c=board.I2C())

### UNTESTED CODE ####

@app.route("/")
def home():
    return redirect("https://keukenmessen.com/", 301)


@app.route("/slice/")
def slice():
    for i in range(80):
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(0.01)
    kit.stepper1.release()
    return {
        "status": "ok",
    }
