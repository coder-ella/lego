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

def Daddy_Dropoff(hub, bob, moyrorL):
    # change the name of this function to what you are doing
    # add required parameters like hub, bob
    # eg of a good name: do_mission_run_1(hub, bob)
    # update the name of your function, 
    # at the end of the code.

    #Clear terminal
    print("\x1b[H\x1b[2J", end="")

    bob.use_gyro(True)
    
    print("Lunching")
    #example
    #bob.straight(200, then=Stop.COAST)
    print(f"bob settings {bob.settings()}")
    # bob settings (st.speed 207, st.accl 720, turn.accl 238, turn rate 450)
    bob.settings(straight_speed=500, straight_acceleration=250, turn_acceleration=100,turn_rate=200)
    hub.light.on(Color.GREEN)
    bob.straight(380)
    bob.straight(-50)
    bob.turn(30)
    bob.straight(500)

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
    Everett_Grace_Function(hub, bob, moyrorL)