from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon       
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# https://docs.pybricks.com/en/latest/robotics.html

#CHANGES TO MAKE
# - 
# - 
# - 

def m_10(hub, bob, moyrorR, moyrorL):
    """
    function for run 1

    
    Arguments:
        hub: the hub
        bob: the drive base
        moyrorR: The right attachment motor
    """
    print("2024-08-25")
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
    print("Leaving Home")
    bob.straight(150)
    bob.turn(-55)
    bob.straight(550)
    print("Initiating Mission 10")
    bob.turn(45)
    bob.straight(350)
    moyrorR.run_angle(400, -280) # Down
    bob.turn(-25)
    moyrorR.run_angle(400, 140) # Up
    print("Mission 10 Complete")
    print("Initiating Mission 5")
    bob.turn(-100)
    moyrorR.run_angle(1000, -120) # Arm down for fishy friend
    bob.straight(140)
    bob.turn(95)
    print("Mission 5 Complete")
    print("Initiating Mission 14_Seabed")
    bob.straight(100)
    moyrorR.run_angle(100, 60)#lift arm up ctr+shift+space=instructions
    bob.turn(11)
    bob.straight(120)
    bob.straight(-50,wait=False)
    moyrorR.run_angle(300, 200)
    #bob.straight(-70)
    #print("Initiating Mission 14_Seabed")
    #bob.turn(-45)
    #bob.straight(330)
    #bob.turn(90)
    #bob.straight(-30)
    #print("Launching Attacment Arm")
    #moyrorR.run_angle(500, -270)
    hub.speaker.play_notes(["D4/8", "C#4/8", "D4/4", "A3/4", "G3/4"])
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