from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def simple_move(hub, bob, motor_attach_left, motor_attach_right):
    #Go forward
    bob.straight(500)
    #Go backward
    bob.straight(-500)
    '''
    #Turn 90 degrees
    bob.turn(90)
    #Turn to other side
    bob.turn(-180)
    #Turn back to facing forward
    bob.turn(90)
    '''
    bob.turn(360)
    motor_attach_left.run_angle(900, (360*4), then=Stop.COAST)
    motor_attach_left.run_angle(-900, (360*4), then=Stop.COAST)

if __name__ == '__main__':
    print("testing")
    hub = InventorHub()
    motor_left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    motor_right = Motor(Port.D,Direction.CLOCKWISE)
    motor_attach_left = Motor(Port.C, Direction.CLOCKWISE,gears=[20,12])
    motor_attach_right = Motor(Port.B, Direction.CLOCKWISE,gears=[20,12])
    bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
    wheel_diameter = 55.6, axle_track = 95)

    simple_move(hub, bob, motor_attach_left, motor_attach_right)