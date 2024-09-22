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
    bob.settings(straight_acceleration= 300, turn_acceleration= 100)
    hub.light.on(Color.GREEN)
    bob.straight(-100) #Starting on 1st bold line on right home - wall square
    
    moyrorR.run_until_stalled(-500,duty_limit=50) #reset arm

    bob.straight(650) #move towards treasure
    bob.turn(81)    #turn towards treasure
    
    bob.settings(straight_speed=200) 
    bob.straight(100)#drive to ship
    bob.turn(5)
    hub.speaker.beep()
    moyrorR.run_angle(200,100,wait=False) #lift arm, dont wait
    bob.straight(50) #drive forward some more
    hub.speaker.beep()

    #drive back
    bob.settings(straight_speed=900, straight_acceleration= 500,
        turn_acceleration= 5000, turn_rate=663)

    bob.straight(-150)
    bob.turn(-82)
    bob.straight(-650)

    moyrorR.run_until_stalled(-500,duty_limit=100)
    

    
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