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

def item_collection(hub, bob, moyrorR, moyrorL):
    """
    function for run 1

    
    Arguments:
        hub: the hub
        bob: the drive base
        moyrorR: The right attachment motor
    """
    print("2024-09-21")
    bob.use_gyro(True)
    #Clear terminal
    print("\x1b[H\x1b[2J", end="")
    
    print("Hold on to your butts...")
    bob.settings(970, 5000)
    bob.settings(straight_acceleration= 300, turn_acceleration= 200)
    hub.light.on(Color.GREEN)
    #bob.straight(-100) #Starting on 1st bold line on right home
    #moyrorR.run_angle(500, 45)
    print("\x1b[H\x1b[2J", end="")

    #Setup at 10 blocks left of the red line at home

    
    print("Wallsquare")
    bob.straight(-5)
    #moyrorR.run_until_stalled(1000,duty_limit=50)
    moyrorR.run_angle(500, 100, wait=False)
    bob.curve(1700,23) # was 1600,23
    
    #hub.speaker.beep(500)
    print("Grab Items")
    bob.curve(25,40) # 2nd parameter was 25, then 35

    bob.settings(straight_speed=970, straight_acceleration=4000) 
    #hub.speaker.beep(2000)
    bob.straight(240)
    '''
    hub.speaker.beep(100)
    bob.straight(50)
    '''
    #hub.speaker.beep(4000)
    bob.turn(35)
    #hub.speaker.beep(8000)
    print("Go to kelp")
    bob.straight(935) # 850
    print("Break")
    bob.settings(straight_acceleration= 200, turn_acceleration= 200)
    wait(200)
    #bob.straight(200)
    #bob.turn(-20)
    print("Go to Home")
    bob.turn(68) # was 60
    bob.settings(straight_acceleration= 900, turn_acceleration= 200)
    bob.straight(600) # was 670
    print("Done")
    moyrorR.run_until_stalled(-1000,duty_limit=50)
    hub.speaker.beep()
    #hub.speaker.play_notes(["D4/8", "C#4/8", "D4/4", "A3/4", "G3/4"])
    hub.display.icon(Icon.SAD)
    #wait(200)
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
    item_collection(hub, bob, moyrorR,moyrorL)