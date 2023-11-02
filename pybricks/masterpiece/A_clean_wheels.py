from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon       
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# https://docs.pybricks.com/en/latest/robotics.html

def clean(hub, bob):
    wait(200)
    bob.straight(700)
    wait(200)
    bob.straight(-700)
    
    hub.speaker.play_notes([
    "G3/4", "G3/4", "G3/4", "C3/4.",  
    "G3/4","F3/4","E3/4","D3/4", "C4/4.",
    "G3/4","F3/4","E3/4","D3/4", "C4/4.",
    "G3/4","F3/4","E3/4","F3/4","D3/4.", 
    ])


# this code allows you to run this code directly without using
# the menu system
if __name__ == '__main__':
    print("testing")
    hub = InventorHub()
    motor_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
    motor_right = Motor(Port.D,Direction.CLOCKWISE)
    bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
    wheel_diameter = 55.6, axle_track = 83.79999999699997)
    clean(hub, bob)
