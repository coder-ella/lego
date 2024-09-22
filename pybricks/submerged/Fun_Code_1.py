from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()
motor_left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.A,Direction.CLOCKWISE)
moyrorR = Motor(Port.F)
moyrorL = Motor(Port.E)

bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
wheel_diameter = 55.6, axle_track = 83.79999999999997)

print("hold onto your butts")
moyrorR.run_angle(500, 20)
moyrorL.run_angle(500, 70)