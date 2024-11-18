from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon       
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# https://docs.pybricks.com/en/latest/robotics.html

def m_09_p2(hub, bob, moyrorR, moyrorL):
    """
    function for run 1

    
    Arguments:
        hub: the hub
        bob: the drive base
        moyrorR: The right attachment motor
    """
    print("2024-10-6")
    #Use this code
    bob.use_gyro(True)
    #Clear terminal
    print("\x1b[H\x1b[2J", end="")
    
    print("Hold on to your butts...")
    bob.settings(970, 5000)
    bob.settings(straight_acceleration= 300, turn_acceleration= 200)
    hub.light.on(Color.GREEN)
    bob.straight(-100) #Starting on 1st bold line on right home'
    print("\x1b[H\x1b[2J", end="")
    print("Initiating Mission 9")
    bob.settings(straight_speed=300, straight_acceleration=5000
    ,turn_rate=663, turn_acceleration=13271)
    hub.speaker.beep()
    bob.settings(straight_speed=970, straight_acceleration=9704
    ,turn_rate=1327, turn_acceleration=13271)
    # change settings back
    bob.settings(straight_acceleration= 300, turn_acceleration= 200)
    print("Leaving Home")
    moyrorR.run_angle(500,-180)
    bob.straight(-20)
    bob.straight(115) # was 100
    print("Initiating Mission 5")
    bob.turn(-51)
    bob.straight(1208)#was 1220, then 1210
    print("Mission 5 Complete")
    print("Initiating Mission 3")
    bob.turn(-11)
    print("Press down on Mission 3")
    moyrorR.run_angle(500, -110) # was 100
    print("Mission 3 Completed")
    moyrorR.run_angle(500,120)
    bob.straight(-200)
    print("Initiating to Mission 2")
    bob.turn(-20)
    bob.straight(551.5) # Was 550, then 552.5
    moyrorR.run_until_stalled(-2000, duty_limit=180) # dl was 100
    #moyrorR.run_angle(500, -160)
    print("Initiating Mission 4")
    bob.straight(-20)
    print("Mission 2 Completed")
    moyrorR.run_angle(500, 70) # was 130, then 75
    hub.speaker.beep()
    print("Turn toward scuba Jimmy")
    bob.turn(-25)
    wait(100)
    print("Attempt to ram Scuba Jimmy")
    bob.straight(100)
    print("Initiating Mission 1")
    print("lift Scuba Jimmy")
    #moyrorR.run_until_stalled(1000, duty_limit=50)
    moyrorR.run_angle(50,32) # 30 was 45
    wait(100)
    bob.straight(-30)
    print("PICK UP DIVER JIMMY GUY MAN BOY2")
    #moyrorR.run_angle(5, 15)
    hub.speaker.beep()
    wait(10)
    hub.speaker.beep()
    print("Mission 1 Completed")
    print("Initiating Mission 4b")
    bob.turn(160)
    moyrorR.run_angle(50, -13) # was -2
    print("drive to the hanging")
    bob.straight(38) # was 40
    bob.turn(-20)
    bob.straight(50)
    print("Mission 4b Completed")
    print("Initiating backup to home")
    bob.turn(-20)
    bob.straight(-850)
    print("Done")
    hub.speaker.play_notes(["D4/8", "C#4/8", "D4/4", "A3/4", "G3/4"])
    hub.display.icon(Icon.HAPPY)
    bob.use_gyro(False)

# this code allows you to run this code directly without using the menu system
if __name__ == '__main__':
    print(__name__)
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
    # hub.speaker.play_notes(["D4/8", "C#4/8", "D4/4", "A3/4", "G3/4"])
    m_09_p2(hub, bob, moyrorR,moyrorL)
