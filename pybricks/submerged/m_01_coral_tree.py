from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon       
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# https://docs.pybricks.com/en/latest/robotics.html

def m_01_coral_tree(hub, bob, moyrorR, moyrorL):
    """
    function for run 1

    
    Arguments:
        hub: the hub
        bob: the drive base
        moyrorR: The right attachment motor
    """
    print("2024-10-06")
    bob.use_gyro(True)
    #Clear terminal
    print("\x1b[H\x1b[2J", end="")
    
    print("Hold on to your butts...")
    bob.settings(970, 5000)
    bob.settings(straight_acceleration= 100, turn_acceleration= 200)
    hub.light.on(Color.GREEN)
    bob.straight(-100) #Starting on 1st bold line on right home
    #moyrorR.run_angle(500, 45)
    print("\x1b[H\x1b[2J", end="")

    print("Wallsquare")
    bob.straight(-10)
    #moyrorR.run_until_stalled(1000,duty_limit=50)
    bob.straight(260)
    #bob.turn(-40)
    #bob.straight(50)
    moyrorR.run_angle(60,110,wait=False)
    bob.straight(200)
    bob.straight(-500)
    print("Done")
    moyrorR.run_until_stalled(-1000,duty_limit=50)
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
    m_01_coral_tree(hub, bob, moyrorR,moyrorL)