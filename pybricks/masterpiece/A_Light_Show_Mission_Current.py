from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon       
from pybricks.robotics import DriveBase, GyroDriveBase
from pybricks.tools import wait, StopWatch

# https://docs.pybricks.com/en/latest/robotics.html

#CHANGES TO MAKE
# - Move less toward augmented reality
# - Perfect turn to get to setup for light show
# - 

def light_show_run(hub, bob, moyrorR):
    """
    function for run 1


    Arguments:
        hub: the hub
        bob: the drive base
        moyrorR: The right attachment motor
    """

    #Clear terminal
    print("\x1b[H\x1b[2J", end="")
   
    print("...")
    #example
    #bob.straight(200, then=Stop.COAST)
    '''
    bob.settings(straight_acceleration= 300, turn_acceleration= 200)
    hub.light.on(Color.GREEN)
    bob.straight(-50)
    print("Wallsquare")
    bob.straight(330)
    print("Go toward printer")
    bob.turn(-45)
    print("Turn toward printer")
    bob.straight(200)
    print("Ram printer")
    bob.straight(-100)
    print("Back away from 4d printer")
    bob.turn(40)
    print("Turns to go forward")
    bob.straight(325)
    print("Forward toward hologram war")
    bob.turn(-130)
    print("Turn toward hologram war")
    bob.straight(-350)
    bob.straight(50)
    bob.turn(35)
    print("Go towards fight show mission")
    bob.straight(525)
    
    print("Augmented Fakeality Mission")
    
    bob.turn(100)
    bob.straight(35)
    bob.settings(straight_speed=900)
    
    moyrorR.run_angle(1001, 600)
    
    bob.settings(straight_speed=600)
    bob.straight(-50)
    bob.settings(straight_speed=300)
    
    print("gotp Light Show Mission")

    bob.turn(90)
    moyrorR.run_angle(-700, 500)
    bob.straight(-180)
    bob.turn(92)'''

    print("start light show mission")
    bob.straight(-500)

    
    moyrorR.run_angle(900,570)

    print("do light show mission")
    bob.settings(straight_speed=150)
    bob.straight(600)
    bob.straight(-30)
    moyrorR.run_angle(-4005, 400)
    
    bob.settings(straight_speed=300)
    bob.straight(-400)
    
    moyrorR.run_time(-1000, 800)
    bob.straight(100)
    bob.turn(19)
    bob.straight(699.6)
    moyrorR.run_angle(9900, 700)
    bob.turn(70)
    moyrorR.run_angle(2982, -700)
    bob.turn(20)
    bob.straight(1000)
    bob.turn(-60)
    bob.straight(1000)


    print("done")
    hub.speaker.play_notes(["C4/4", "C4/4", "G4/4", "G4/4"])
    hub.display.icon(Icon.HAPPY)
    wait(200)


# this code allows you to run this code directly without using
# the menu system
if __name__ == '__main__':
    print("testing")
    hub = InventorHub()
    motor_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
    motor_right = Motor(Port.D,Direction.CLOCKWISE)
    moyrorR = Motor(Port.B)
    #try GyroDriveBase
    bob = GyroDriveBase(left_motor = motor_left, right_motor=motor_right,
    wheel_diameter = 55.6, axle_track = 83.79999999699997)


    # call your function.
    # remember to rename the below name to match
    # your function name on line 11
    light_show_run(hub, bob, moyrorR)
