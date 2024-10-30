from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon       
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

from pybricks.tools import multitask, run_task

# https://docs.pybricks.com/en/latest/robotics.html

#CHANGES TO MAKE
# - 
# - 
# - 

def jurasic_park_theme(hub, bob, moyrorR, moyrorL):
    hub.display.icon(Icon.HEART)

    x = hub.speaker.play_notes(notes = [
        "D3/8", "C#3/8", "D3/4", "A2/4", "G2/4", 
        "D3/8", "C#3/8", "D3/4", "A2/4", "G2/4", 
        "D3/8", "C#3/8", "C#3/8","D3/2", "A2/4", 
        "D2/4", "C3/2",  "D3/8", "C#3/8","D3/4", 
        "A2/4", "G2/4",  "D3/8", "C#3/8","D3/4", 
        "A2/4", "G2/4",  "D3/8", "C#3/8","C#3/8", 
        "D3/2", "A2/4",  "D2/4", "D3/2", "C#3/2", 
        "D3/1"
        "D3/8", "C#3/8", "D3/4", "A2/4", "G2/4", 
        "D3/8", "C#3/8", "D3/4", "A2/4", "G2/4", 
        "D3/8", "C#3/8", "C#3/8","D3/2", "A2/4", 
        "D2/4", "C3/2",  "D3/8", "C#3/8","D3/4", 
        "A2/4", "G2/4",  "D3/8", "C#3/8","D3/4", 
        "A2/4", "G2/4",  "D3/8", "C#3/8","C#3/8", 
        "D3/2", "A2/4",  "D2/4", "D3/2", "C#3/2", 
        "D3/1"
        ],tempo=220)
    
    

    hub.display.icon(Icon.HAPPY)
    

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
    jurasic_park_theme(hub, bob, moyrorR,moyrorL)
    