from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon       
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# https://docs.pybricks.com/en/latest/robotics.html

def kelp_mission(hub, bob, moyrorR, moyrorL):
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
    bob.settings(straight_acceleration= 300, turn_acceleration= 200)
    hub.light.on(Color.GREEN)
    #bob.straight(-100) #Starting on 1st bold line on right home
    #moyrorR.run_angle(500, 300)
    print("\x1b[H\x1b[2J", end="")

    #moyrorR.run_angle(-)
    #bob.settings(straight_speed=485, straight_acceleration=9704
    #,turn_rate=663, turn_acceleration=13271) 
    #moyrorR.run_angle(50,50,wait=False)
    #bob.turn(45)
    """
    moyrorR.run_until_stalled(1000,duty_limit=50)
    bob.straight(800)
    bob.turn(90)
    bob.straight(20)
    moyrorR.run_until_stalled(-1000,duty_limit=50)
    bob.straight(-1000)
    bob.turn(-20)
    bob.straight(-300)
    bob.turn(-60)
    bob.straight(-700)
    """
    moyrorR.run_angle(300, 100)
    bob.straight(900)
    bob.turn(-65)
    bob.straight(20)
    moyrorR.run_angle(300, -130)
    hub.speaker.beep()
    wait(100)
    bob.straight(-30)
    bob.turn(-45)
    moyrorR.run_angle(300,100)
    bob.straight(-30)
    bob.turn(-130)
    bob.straight(15)
    moyrorR.run_until_stalled(-1000,duty_limit=50)
    bob.straight(-30)
    bob.turn(45)
    bob.straight(-200)
    bob.straight(-10)
    hub.speaker.beep()
    wait(500)
    bob.straight(500)

    
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
    kelp_mission(hub, bob, moyrorR,moyrorL)
