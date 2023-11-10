from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()
motor_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.D,Direction.CLOCKWISE)
moyrorR = Motor(Port.B)
bob = DriveBase(left_motor = motor_left, right_motor=motor_right, 
wheel_diameter = 55.6, axle_track = 83.79999999699997)
bob.settings(turn_acceleration=450)
    
moyrorR.run_angle(10000, -300, wait=False)
bob.straight(-100)
bob.straight(500)
bob.straight(-500)
moyrorR.run_angle(900, 300, wait=False)
bob.straight(-100)