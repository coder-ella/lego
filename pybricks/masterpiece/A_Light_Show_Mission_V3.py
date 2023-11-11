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

def light_show_run(hub, bob, moyrorR, moyrorL):
    """
    function for run 1

    
    Arguments:
        hub: the hub
        bob: the drive base
        moyrorR: The right attachment motor
    """
    print("11-7-2023")
    ratio = 1.8
    bob.use_gyro(True)
    #Clear terminal
    print("\x1b[H\x1b[2J", end="")
    
    print("...")
    bob.settings(straight_acceleration= 300, turn_acceleration= 200)
    hub.light.on(Color.GREEN)
    print("Wallsquare")
    bob.straight(-50)
    print("Go toward printer")
    bob.straight(330)
    print("Turn toward printer")
    bob.turn(-45)
    print("Ram printer")
    bob.straight(200)
    print("Back away from printer")
    bob.straight(-100)
    print("Turns to go forward")
    bob.turn(40)
    print("Forward toward hologram mission")
    bob.straight(325)
    print("Turn toward hologram mission")
    bob.turn(-130)
    print("Ram hologram mission")
    bob.straight(-350)
    print("Back away from hologram mission")
    bob.straight(50)
    print("Turn to go towards light show mission")
    bob.turn(35)
    print("Go towards light show mission")
    bob.straight(525)
    print("Augmented Fakeality Mission")
    
    bob.turn(105)
    bob.straight(60)
    bob.settings(straight_speed=900)
    
    moyrorR.run_angle(1001, 650*ratio)
    
    bob.settings(straight_speed=600)
    bob.straight(-60)
    bob.settings(straight_speed=300)
    
    print("go to Light Show Mission")

    bob.turn(90)
    moyrorR.run_angle(-1000, 700*ratio, wait=False)
    bob.straight(-180)
    bob.turn(90)
    bob.straight(75)
    print("Do light show mission")
    moyrorL.run_angle(1000, 3390)
    bob.straight(-100)
    #bob.settings(straight_speed=60)
    #bob.straight(100)
    hub.speaker.beep()
    print("Turn towards camera mission") 
        
    print("Dont Grab Camera")
    bob.turn(38)
    bob.straight(1000)


    print("done")
    #hub.speaker.play_notes(["C4/4", "C4/4", "G4/4", "G4/4"])
    #hub.display.icon(Icon.HAPPY)
    wait(200)
    bob.use_gyro(False)
    

# this code allows you to run this code directly without using
# the menu system
if __name__ == '__main__':
    print("testing")
    hub = InventorHub()
    motor_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
    motor_right = Motor(Port.D,Direction.CLOCKWISE)
    moyrorR = Motor(Port.B)
    moyrorL = Motor(Port.A)
    bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
    wheel_diameter = 55.6, axle_track = 83.79999999699997)

    # call your function.
    # remember to rename the below name to match
    # your function name on line 11
    light_show_run(hub, bob, moyrorR,motor_left)