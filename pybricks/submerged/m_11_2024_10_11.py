from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon       
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
#from A_fn_diagnostics import run_diagnostics

# https://docs.pybricks.com/en/latest/robotics.html
'''
# default settings
bob.settings(straight_speed=194, straight_acceleration=727
    ,turn_rate=221, turn_acceleration=995)
#max values allowed
bob.settings(straight_speed=970, straight_acceleration=9704
    ,turn_rate=1327, turn_acceleration=13271) 
# high speed
bob.settings(straight_speed=485, straight_acceleration=9704
    ,turn_rate=663, turn_acceleration=13271) 
'''

def kelp_mission(hub, bob, moyrorR, moyrorL):
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
    #bob.straight(-100) #Starting on 1st bold line on right home
    #moyrorR.run_angle(500, 300)
    print("\x1b[H\x1b[2J", end="")

    '''
    moyrorR.run_angle(300, 100)
    bob.straight(900)
    bob.turn(-65)
    bob.straight(60) # was 20
    # Grab yellow beam for radar mission
    moyrorR.run_angle(300, -130)
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
    bob.reset()
    bob.turn(10)
    hub.speaker.beep()
    wait(500)
    bob.straight(900)
    '''
   #moyrorR.run_until_stalled(-100,duty_limit=50)

   #Start on first black line from the left and move it a half-centimeter to the right
   
   #For Next Meeting
   # - Get this consistent
   # - Lift after pulling over first time
   # - Doesn't need to use yellow arm for second part
   # - Rewatch video?
    #moyrorR.run_until_stalled(-100)
    #moyrorR.reset_angle()
    print("Wallsquare")
    moyrorR.run_angle(100,50)
    bob.straight(-50)
    print("Head to Mission 11")
    bob.straight(700)
    bob.turn(-90)
    bob.straight(175)
    # go to 
    bob.turn(90)
    print("Face Mission 11")
    bob.straight(110)
    moyrorR.run_angle(100,-42)
    bob.straight(-83)
    hub.speaker.beep()
    # lift arm from sonar, for collab mission
    moyrorR.run_angle(100,33) # was 30
    print("Go to Mission 10")
    bob.turn(-60) # changed again, was 58
    moyrorR.run_angle(200,-5)
    bob.straight(330)
    #change to run until stalled
    #moyrorR.run_angle(100,90)
    print("Lift Up Collab Mission")
    moyrorR.run_until_stalled(100,duty_limit=199) # was 150
    bob.straight(-150) # was -100
    bob.turn(-28)
    print("Go towards Sand Sample")
    moyrorR.run_angle(100,70)
    # drive forward towards seabed and glowfish (perpendicular to seabed)
    bob.straight(468) # was 470
    bob.turn(90)
    # back imto fish 
    bob.straight(-100) # was -135
    # arm down to reset (Seabed sample)
    moyrorR.run_until_stalled(-200,duty_limit=80)
    hub.speaker.beep()
    # raise arm for seabed sample
    moyrorR.run_angle(100,73) # was 60
    bob.straight(90) # go to grab seabed sample, was 150
    moyrorR.run_angle(70,100)
    bob.straight(-45) # was 150
    print("Mission Sand Sample Complete")
    print("Drive at kelp")
    bob.turn(90)
    bob.straight(780)
    bob.turn(-20)
    moyrorR.run_until_stalled(-1000,duty_limit=50)
    bob.straight(-100)
    bob.turn(90)
    bob.straight(550)
    hub.speaker.beep()

    """
    print("Lift Arm After 1st Whale")
    moyrorR.run_angle(100,45)
    bob.turn(-20)
    bob.straight(-35)
    moyrorR.run_angle(100,-33)
    bob.straight(75)
    return
    """
    '''
    bob.turn(-30)
    bob.turn(20)
    moyrorR.run_angle(100,20)
    bob.straight(50)
    moyrorR.run_angle(100,100)
    bob.straight(-800)
    '''
    """
    bob.settings(straight_speed=970, straight_acceleration=9704
    ,turn_rate=1327, turn_acceleration=13271) 
    bob.straight(1000)
    moyrorR.run_angle(100,100)
    bob.turn(690)
    bob.straight(100)
    moyrorR.run_until_stalled(-100,duty_limit=50)
    """
    print("Done")
    moyrorR.run_until_stalled(-1000,duty_limit=50)
    hub.speaker.play_notes(["D4/8", "C#4/8", "D4/4", "A3/4", "G3/4"])
    hub.display.icon(Icon.HAPPY)
    wait(200)
    bob.use_gyro(False)


# this code allows you to run this code directly without using
# the menu system
if __name__ == '__main__':
    print(__name__)

    hub = InventorHub()
    #run_diagnostics(hub)

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