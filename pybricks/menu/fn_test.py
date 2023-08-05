# this file represents a template for writing code that can then be imported
# and called from the main_menu.

from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def move_forward(bob):
    bob.straight(200, then=Stop.COAST)

def move_back(bob):
    bob.straight(-200, then=Stop.COAST)

def turn_45_r(bob):
    bob.turn(45, then=Stop.COAST)

def turn_45_l(bob):
    bob.turn(-45, then=Stop.COAST)

if __name__ == '__main__':
    # this section of the code allows for testing of this file
    # without needing to use the main-menu
    print("testing")
    hub = InventorHub()
    motor_left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    motor_right = Motor(Port.D,Direction.CLOCKWISE)
    bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
    wheel_diameter = 55.6, axle_track = 95)

    motor_attach_left = Motor(Port.C, Direction.CLOCKWISE,gears=[20,12])
    motor_attach_right = Motor(Port.B, Direction.CLOCKWISE,gears=[20,12])
    sensor = ColorSensor(Port.F)
    sensor_2 = ColorSensor(Port.E)

    move_forward(bob)
    turn_45_l(bob)
