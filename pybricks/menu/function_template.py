from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# copy this entire file and name it something like
# mission_run_1.py
# it will allow the code to be later included in the menu

def do_mission_run_template(hub, bob):
    # change the name of this function to what you are doing
    # add required parameters like hub, bob
    # eg of a good name: do_mission_run_1(hub, bob)
    # update the name of your function, 
    # at the end of the code.

    #Clear terminal
    print("\x1b[H\x1b[2J", end="")
    
    print("doing stuff")
    #example
    bob.straight(200, then=Stop.COAST)
    hub.light.on(Color.GREEN)

# dont write any code below this.
# this code allows you to run this code directly without using
# the menu system
if __name__ == '__main__':
    print("testing")
    hub = InventorHub()
    motor_left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    motor_right = Motor(Port.D,Direction.CLOCKWISE)
    bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
    wheel_diameter = 55.6, axle_track = 95)

    # call your function. 
    # remember to rename the below name to match
    # your function name on line 11
    do_mission_run_template(hub, bob)
