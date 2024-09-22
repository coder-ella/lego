from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon       
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# https://docs.pybricks.com/en/latest/robotics.html

#CHANGES TO MAKE
# - Move less toward augmented reality
# - Perfect turn to get to setup for light show
# - 


# this code allows you to run this code directly without using
# the menu system
# moyrorR.run_until_stalled(-1000, duty_limit=90)
# voltage = hub.battery.voltage()
# VMAX = 8300
# VMIN = 6000
if __name__ == '__main__':
    print("testing")
    hub = InventorHub()
    motor_left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    motor_right = Motor(Port.B,Direction.CLOCKWISE)
    moyrorR = Motor(Port.F)
    moyrorL = Motor(Port.E)
    bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
    wheel_diameter = 55.6, axle_track = 83.79999999999997)

    #moyrorR.run_angle(600,-250)
    moyrorR.run_until_stalled(-1000,duty_limit=50)
    hub.speaker.play_notes(["D4/8", "C#4/8", "D4/4", "A3/4", "G3/4"])
    bob.straight(100)
    
    
    
    
