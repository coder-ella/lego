from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


def Everett_Grace_Function(hub, bob, moyrorL):
    # change the name of this function to what you are doing
    # add required parameters like hub, bob
    # eg of a good name: do_mission_run_1(hub, bob)
    # update the name of your function, 
    # at the end of the code.

    #Clear terminal
    print("\x1b[H\x1b[2J", end="")
    
    print("Lunching")
    #example
    #bob.straight(200, then=Stop.COAST)
    print(f"bob settings {bob.settings()}")
    # bob settings (st.speed 207, st.accl 720, turn.accl 238, turn rate 450)
    bob.settings(straight_acceleration=250, turn_acceleration=100,turn_rate=200)
    hub.light.on(Color.GREEN)
    # square up against wall
    bob.straight(10)
    bob.straight(-20)
    
    #step 1 drive towards light tower
    bob.straight(40)
    bob.turn(65.2569)
    wait(10)

    #drive to museum
    bob.straight(1000)
    wait(10)
    
   
    wait(10)
    # Back up
    bob.straight(-290)
    wait(100)
    Stop
    bob.turn(-35)
    bob.stop()
    wait(500)
    bob.straight(50)
    
    #drive to vr
    bob.straight(90)
    wait(10)
    moyrorL.run_angle(1300,-1150)
    print(moyrorL.control.limits())

    #back up from vr
    bob.straight(-75)

    #turn towards mission 2
    moyrorL.run_angle(600,20.5)
    bob.stop
    bob.turn(-65)
    bob.straight(370)

    #bob do misson 2 sucsessfully
    bob.straight(80)
    bob.straight(-80)
    bob.straight(80)
    bob.straight(-80)
    bob.straight(80)
    bob.straight(-80)
    bob.straight(80)
    bob.straight(-80)





    #print("\x1b[H\x1b[2J", end="")
    #print("Lunch Complete")

if __name__ == '__main__':
    print("Preparing to Lunch")
    hub = InventorHub()
    motor_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
    motor_right = Motor(Port.D,Direction.CLOCKWISE)
    moyrorL = Motor(Port.A)
    bob = DriveBase(left_motor = motor_left, right_motor=motor_right, wheel_diameter = 55.6, axle_track = 83.79999999699997)
    bob.settings(turn_acceleration=450)
    Everett_Grace_Function(hub, bob, moyrorL)
