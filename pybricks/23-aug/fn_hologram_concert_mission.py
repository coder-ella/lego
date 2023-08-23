from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# copy this entire file and name it something like
# mission_run_1.py
# it will allow the code to be later included in the menu

def do_mission_hologram_concert(hub, bob, attach_motor_left, attach_motor_right):
    #Clear terminal
    
    print("\x1b[H\x1b[2J", end="")
    bob.straight(-10)
    bob.straight(725)
    bob.turn(45)
    bob.straight(130)
    




# dont write any code below this.
# this code allows you to run this code directly without using
# the menu system
if __name__ == '__main__':
    print("testing")
    hub = InventorHub()
    motor_left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    motor_right = Motor(Port.D,Direction.CLOCKWISE)
    attach_motor_left = Motor(Port.C, Direction.CLOCKWISE)
    attach_motor_right = Motor(Port.B, Direction.CLOCKWISE)
    bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
    wheel_diameter = 55.6, axle_track = 95)

    # call your function. 
    # remember to rename the below name to match
    # your function name on line 11
    do_mission_hologram_concert(hub, bob, attach_motor_left, attach_motor_right)