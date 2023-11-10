from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
"""
Robot: Not Bob
Home: Left side of board
Attachments: Front fork + original mantis arm
"""

def longy(hub, bob, moyrorL):
    # change the name of this function to what you are doing
    # add required parameters like hub, bob
    # eg of a good name: do_mission_run_1(hub, bob)
    # update the name of your function, 
    # at the end of the code.

    #Clear terminal
    print("\x1b[H\x1b[2J", end="")

    print(f"Ready: {hub.imu.ready()}")

    bob.use_gyro(True)
    
    print("Lunching")
    #example
    #bob.straight(200, then=Stop.COAST)
    print(f"bob settings {bob.settings()}")
    # bob settings (st.speed 207, st.accl 720, turn.accl 238, turn rate 450)
    
    bob.settings(straight_acceleration=250, turn_acceleration=100,turn_rate=200)
    hub.light.on(Color.GREEN)
    

    bob.settings(75)
    bob.straight(380)
    bob.settings(970, turn_acceleration=150)
    bob.straight(-210)
    bob.turn(25)
    bob.straight(70)
    bob.turn(15)
    bob.straight(100)
    bob.turn(28)
    bob.straight(125)
    bob.turn(120)
    bob.straight(200)

    print("me done now")
if __name__ == '__main__':
    print("Preparing to Lunch")
    hub = InventorHub()
    motor_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
    motor_right = Motor(Port.D,Direction.CLOCKWISE)
    moyrorL = Motor(Port.A)
    #try GyroDriveBase
    bob = DriveBase(left_motor = motor_left, right_motor=motor_right, 
    wheel_diameter = 55.6, axle_track = 83.79999999699997)
    bob.settings(turn_acceleration=450)
    longy(hub, bob, moyrorL)