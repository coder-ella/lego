from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

from common_function1 import wallsquare

hub = InventorHub()

left_motor = Motor(Port.B, Direction.CLOCKWISE)
right_motor = Motor(Port.A,Direction.COUNTERCLOCKWISE)

attach_motor_left = Motor(Port.C, Direction.CLOCKWISE)
gear_ratio = 20/12
#print(1.67)

#attach_motor_left.run_angle( 900,2*360*gear_ratio)

drive_base = DriveBase(left_motor, 
    right_motor, 
    wheel_diameter = 55.6,
    axle_track= 95)

wait(1000)
wallsquare(drive_base)



drive_base.straight(300)
drive_base.turn(-45)
drive_base.straight(340)
attach_motor_left.run(900)
drive_base.turn(-42)
drive_base.straight(400)
attach_motor_left.brake()
drive_base.turn(-90)
drive_base.straight(500)
