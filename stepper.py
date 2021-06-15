import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
kit = MotorKit(i2c=board.I2C())

for i in range(80):
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    time.sleep(0.01)
kit.stepper1.release()
