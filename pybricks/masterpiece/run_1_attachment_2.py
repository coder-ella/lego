from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop       
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


# copy this entire file and name it something like
# mission_run_1.py
# it will allow the code to be later included in the menu


def Everett_Grace_Function(hub, bob, moyrorR):
    #Clear terminal
    print("\x1b[H\x1b[2J", end="")
   
    print("...")
    
    bob.settings(straight_acceleration= +300, turn_acceleration= +200)
    hub.light.on(Color.GREEN)
    bob.straight(-50)
    # Wallsquare
    bob.straight(330)
    # Go toward printer
    bob.turn(-45)
    # Turn toward printer
    bob.straight(200)
    # Ram printer
    bob.straight(-100)
    # Back away from 4d printer
    bob.turn(40)
    # Turns to go forward
    bob.straight(325)
    # Forward toward hologram war
    bob.turn(-130)
    # Turn toward hologram war
    bob.straight(-250)
    bob.straight(20)
    bob.turn(35)
    # Go towards light show mission
    bob.straight(550)
    
    # Augmented Fakeality Mission
    bob.turn(100)
    bob.straight(35)
    bob.settings(900)

    # Put arm down to move lever
    moyrorR.run_angle(1001, 600)

    # Slowly move robot back to move lever
    bob.settings(600)
    bob.straight(-250)
    bob.settings(300)
    
    # Light Show Mission

    
    bob.straight(160)
    bob.turn(90)
    moyrorR.run_angle(-700, 500)
    bob.straight(-200)
    bob.turn(92)
    bob.straight(-500)
    
    moyrorR.run_angle(90)

    #Do lightshow mission

    #Drive to mission
    bob.straight(600)
    # Lift arms to raise light pointer
    moyrorR.run_angle(-75, 230)

    # Back up from Light Show and square against wall
    bob.straight(-400)

    # Find out if we need this code (go to camera mission)
    moyrorR.run_time(-1000, 800)
    bob.straight(100)
    bob.turn(30)
    bob.straight(700)


# this code allows you to run this code directly without using
# the menu system
if __name__ == '__main__':
    print("testing")
    hub = InventorHub()
    motor_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
    motor_right = Motor(Port.D,Direction.CLOCKWISE)
    moyrorR = Motor(Port.B)
    bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
    wheel_diameter = +55.6, axle_track = +83.79999999699997)


    # call your function.
    # remember to rename the below name to match
    # your function name on line 11
    Everett_Grace_Function(hub, bob, moyrorR)

