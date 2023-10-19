from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop       
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


# copy this entire file and name it something like
# mission_run_1.py
# it will allow the code to be later included in the menu

#CHANGES TO MAKE
# - Move less toward augmented reality
# - Perfect turn to get to setup for light show
# - 

def Everett_Grace_Function(hub, bob, moyrorR):
    # change the name of this function to what you are doing
    # add required parameters like hub, bob
    # eg of a good name: do_mission_run_1(hub, bob)
    # update the name of your function,
    # at the end of the code.


    #Clear terminal
    print("\x1b[H\x1b[2J", end="")
   
    print("...")
    #example
    #bob.straight(200, then=Stop.COAST)
    
    bob.settings(straight_acceleration= 300, turn_acceleration= 200)
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
    bob.straight(-350)
    bob.straight(50)
    bob.turn(35)
    # Go towards fight show mission
    bob.straight(550)
    
    # Augmented Fakeality Mission
    
    bob.turn(111)
    bob.straight(35)
    bob.settings(straight_speed=900)
    
    moyrorR.run_angle(1001, 600)
    
    bob.settings(straight_speed=600)
    bob.straight(-50)
    bob.settings(straight_speed=300)
    
    # Light Show Mission

    # Ella to check this
    # bob.straight(00)
    bob.turn(90)
    moyrorR.run_angle(-700, 500)
    bob.straight(-200)
    bob.turn(92)
    bob.straight(-500)

    
    moyrorR.run_angle(900,90)

    #Do lightshow mission
    bob.straight(600)
    moyrorR.run_angle(-75, 230)
    
    bob.settings(straight_speed=300)
    bob.straight(-400)
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
    wheel_diameter = 55.6, axle_track = 83.79999999699997)


    # call your function.
    # remember to rename the below name to match
    # your function name on line 11
    Everett_Grace_Function(hub, bob, moyrorR)
