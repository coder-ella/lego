from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon       
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from item_collection_test_run_cablooie_2 import item_collection

# https://docs.pybricks.com/en/latest/robotics.html

#CHANGES TO MAKE
# - 
# - 
# - 

def mast_lift(hub, bob, moyrorR, moyrorL):
    """
    function for run 1

    
    Arguments:
        hub: the hub
        bob: the drive base
        moyrorR: The right attachment motor
    """
    print("2024-10-13")
    bob.use_gyro(True)
    #Clear terminal
    print("\x1b[H\x1b[2J", end="")
    
    print("Hold on to your butts...")
    bob.settings(970, 5000)
    bob.settings(straight_speed=250, straight_acceleration=600
    ,turn_rate=150, turn_acceleration=700)
    hub.light.on(Color.GREEN)
    bob.straight(-10) #Starting on 1st bold line on right home
    #moyrorR.run_angle(500, 45)
    print("\x1b[H\x1b[2J", end="")

    print("Move Forward and Raise the Mast")
    bob.straight(450)
    bob.turn(80)
    bob.straight(200)
    bob.straight(-220)
    bob.turn(-80)
    bob.straight(-500)

    
    hub.display.icon(Icon.SAD)
    wait(200)
    bob.use_gyro(False)
    

# this code allows you to run this code directly without using
# the menu system
if __name__ == '__main__':
    print("testing")
    hub = InventorHub()
    motor_left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
    motor_right = Motor(Port.A,Direction.CLOCKWISE)
    moyrorR = Motor(Port.F)
    moyrorL = Motor(Port.E)
    bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
    wheel_diameter = 55.6, axle_track = 83.79999999999997)

    # call your function.
    # remember to rename the below name to match
    # your function name on line 11
    mast_lift(hub, bob, moyrorR,moyrorL)
    # wait(3000)
    #item_collection(hub, bob, moyrorR, moyrorL)