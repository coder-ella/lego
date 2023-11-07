from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase, GyroDriveBase
from pybricks.tools import wait, StopWatch

"""
Robot: Joe
Home: Left side of board
Attachments: Front fork + original mantis arm
"""

def Everett_Grace_Function(hub, bob, moyrorL):
    # change the name of this function to what you are doing
    # add required parameters like hub, bob
    # eg of a good name: do_mission_run_1(hub, bob)
    # update the name of your function, 
    # at the end of the code.

    #Clear terminal
    print("\x1b[H\x1b[2J", end="")

    #bob.use_gyro(True)
    
    print("Lunching")
    #example
    #bob.straight(200, then=Stop.COAST)
    print(f"bob settings {bob.settings()}")
    # bob settings (st.speed 207, st.accl 720, turn.accl 238, turn rate 450)
    bob.settings(straight_acceleration=250, turn_acceleration=100,turn_rate=200)
    hub.light.on(Color.GREEN)

    
    print("square up against wall")
    bob.straight(10)
    bob.straight(-20)
    
    print("step 1 drive towards light tower")
    bob.straight(50)
    bob.turn(38)
    wait(10)

    print("drive to museum")
    bob.straight(1000)
    wait(10)
    
   
    wait(10)
    # Back up
    bob.straight(-290)
    wait(10)
    bob.turn(-30)
    bob.stop()
    wait(500)
    #bob.straight(50)
    
    #drive to vr
    bob.straight(190)
    bob.straight(-40)
    wait(10)
    moyrorL.run_angle(1300,-1150)
    print(moyrorL.control.limits())

    print("back of from VR")
    bob.straight(-55)
    bob.stop()
  

    print("Lifting attachment")
    moyrorL.run_angle(600, 20)

    print("turn towards Sam")
    bob.stop()
    bob.straight(-65)
    bob.turn(-65)
    wait(10)
    moyrorL.run_angle(600, -150)

    print("go towards Sam")
    bob.straight(430)
    moyrorL.run_angle(600, 360)



    #bad code :(
    '''bob.turn(-80)
    bob.straight(400)
    moyrorL.run_angle(900, 180)
    bob.turn(10)
    moyrorL.run_angle(700, 7)
    hub.speaker.beep(100)
    
    #bob do misson 2 successfully
    bob.settings(straight_speed=500)
    moyrorL.run_angle(900, -360)
    moyrorL.run_angle(900, 360)
    moyrorL.run_angle(900, -360)
    
    bob.straight(130)
    bob.straight(-80)
    bob.straight(100)
    bob.straight(-80)
    bob.straight(100)
    bob.straight(-80)
    
    bob.settings(straight_speed = 194)
    bob.straight(80)
    bob.straight(-80)'''

    print("Ready to send home")


    #print("\x1b[H\x1b[2J", end="")
    print("Lunch Complete")

    #bob.use_gyro(False)

if __name__ == '__main__':
    print("Preparing to Lunch")
    hub = InventorHub()
    motor_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
    motor_right = Motor(Port.D,Direction.CLOCKWISE)
    moyrorL = Motor(Port.A)
    #try GyroDriveBase
    bob = GyroDriveBase(left_motor = motor_left, right_motor=motor_right, 
    wheel_diameter = 55.6, axle_track = 83.79999999699997)
    bob.settings(turn_acceleration=450)
    Everett_Grace_Function(hub, bob, moyrorL)
