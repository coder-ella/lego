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

def m_10_1(hub, bob, moyrorR, moyrorL):
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
    bob.settings(straight_acceleration= 300, turn_acceleration= 200)
    hub.light.on(Color.GREEN)
    bob.straight(-100) #Starting on 1st bold line on right home
    #moyrorR.run_angle(500, 45)
    print("\x1b[H\x1b[2J", end="")

    print("Wallsquare")
    bob.straight(-10)
    print("Heading to Mission 14_Trident")
    moyrorR.run_until_stalled(1000,duty_limit=50)
    bob.straight(30)
    bob.turn(46)
    bob.straight(450)
    print("Initiating Mission 14_Trident")
    moyrorR.run_angle(250,-250)
    bob.straight(-200)
    print("Mission 14_Trident Completed")
    bob.settings(straight_acceleration=9704)
    print("GO HOME")
    bob.straight(-100)
    bob.turn(45)
    bob.straight(-400)
    moyrorR.run_until_stalled(1000,duty_limit=50)
    #bob.turn(-45)
    '''
    print("Wallsquare")
    bob.straight(-250)
    bob.settings(straight_acceleration=727)
    print("Initiate Mission 6")
    #bob.straight(370)
    bob.turn(35)
    bob.straight(10)
    bob.straight(50, wait=False)
    moyrorR.run_angle(100, 270)
    bob.straight(-50)
    print("Mission 6 Completed")
    print("Done")
    '''
    
    #input("Play beautiful music?")
    #Do delete pleeeease I worked hard
    '''
    hub.speaker.play_notes(["D4/8", "C#4/8", "D4/4", "A3/4", "G3/4", "D4/8", 
    "C#4/8", "D4/4", "A3/4", "G3/4", "D4/8", "C#4/8", "C#4/8", "D4/2", "A3/4", 
    "D3/4", "C4/2", "D4/8", "C#4/8", "D4/4", "A3/4", "G3/4", "D4/8", "C#4/8", 
    "D4/4", "A3/4", "G3/4", "D4/8", "C#4/8", "C#4/8", "D4/2", "A3/4", "D3/4", 
    "D4/2", "C#4/2", "D4/1"])
    '''
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
    m_10(hub, bob, moyrorR,moyrorL)
   # wait(3000)
    #item_collection(hub, bob, moyrorR, moyrorL)