from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon       
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# https://docs.pybricks.com/en/latest/robotics.html

'''
# default settings
bob.settings(straight_speed=194, straight_acceleration=727
    ,turn_rate=221, turn_acceleration=995)

#max values allowed
bob.settings(straight_speed=970, straight_acceleration=9704
    ,turn_rate=1327, turn_acceleration=13271) 
# high speed
bob.settings(straight_speed=485, straight_acceleration=9704
    ,turn_rate=663, turn_acceleration=13271) 
'''

def clean(hub, bob):
    # Clear terminal
    print("\x1b[H\x1b[2J", end="")
    default_settings = bob.settings()
    print(default_settings)
    
    bob.settings(straight_speed=485, straight_acceleration=9704,turn_rate=663, turn_acceleration=13271) 
    wait(200)
    bob.straight(2000)

    bob.settings(straight_speed=485, straight_acceleration=9704,turn_rate=663, turn_acceleration=13271) 
    wait(200)
    bob.straight(-2000)

    bob.settings(default_settings[0],default_settings[1],default_settings[2],default_settings[3])
    bob.straight(1000)
        
    hub.speaker.play_notes([
    "G3/4", "G3/4", "G3/4", "C3/4.",  
    "G3/4","F3/4","E3/4","D3/4", "C4/4.",
    "G3/4","F3/4","E3/4","D3/4", "C4/4.",
    "G3/4","F3/4","E3/4","F3/4","D3/4.", 
    ])
    
    print("done")


# this code allows you to run this code directly without using
# the menu system
if __name__ == '__main__':
    hub = InventorHub()
    motor_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
    motor_right = Motor(Port.D,Direction.CLOCKWISE)
    bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
    wheel_diameter = 55.6, axle_track = 83.79999999699997)
    clean(hub, bob)