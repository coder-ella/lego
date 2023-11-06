from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

"""
Robot: Joe
Home: Left side of board
Attachments: Front fork + original mantis arm
"""

def run_theater(hub, bob, moyrorL,count):
    # change the name of this function to what you are doing
    # add required parameters like hub, bob
    # eg of a good name: do_mission_run_1(hub, bob)
    # update the name of your function, 
    # at the end of the code.

    #Clear terminal
    print("\x1b[H\x1b[2J", end="")
    print("V1.1")

    bob.use_gyro(True)
    
    print("Lunching")
    #example
    #bob.straight(200, then=Stop.COAST)
    print(f"bob settings {bob.settings()}")
    # bob settings (st.speed 207, st.accl 720, turn.accl 238, turn rate 450)
    
    #set up at the closest bold line to the camera mission to the edge of robot
    #take off trident holder thing

    bob.straight(-10)

    print("get to stage")
    moyrorL.run_angle(900,-40)
    wait(100)
    moyrorL.run_angle(900, 22)
    bob.straight(600)
    bob.turn(40)
    bob.straight(120)
    bob.turn(-90)

    print("do stage")
    bob.straight(60)
    bob.straight(-60)
    for bump in range(1,count):

        bob.straight(70 +(bump*10))
        hub.speaker.beep()
        wait(100)
        bob.straight(-70 -(bump*10))
        

    print("go home")
    bob.settings(straight_speed=700)
    bob.turn(70)
    bob.straight(-1000)


    #print("\x1b[H\x1b[2J", end="")
    print("Lunch Complete")

    bob.use_gyro(False)

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
    run_theater(hub, bob, moyrorL,2)
