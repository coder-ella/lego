from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#Clear terminal
print("\x1b[H\x1b[2J", end="")

hub = InventorHub()
motor_left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.D,Direction.CLOCKWISE)
motor_attach_left = Motor(Port.C, Direction.CLOCKWISE,gears=[20,12])
motor_attach_right = Motor(Port.B, Direction.CLOCKWISE,gears=[20,12])
sensor = ColorSensor(Port.F)
sensor_2 = ColorSensor(Port.E)
bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
wheel_diameter = 55.6, axle_track = 95)

THRESHOLD = 55
SPEED = 140
KP = 1
#Constant of proportionality for moving
exit_var = 0
#How many times right color sensor has seen black in a row

#55, 0.25 - 43, 0.25 work for THRESHOLD, SPEED, and KP 

bob.settings(straight_speed=100,
straight_acceleration=100)

bob.straight(50)
#Go to the line from home

while True:
    wait(1)
    refl_left = sensor.reflection()
    refl_right = sensor_2.reflection()
    steering = (refl_left - THRESHOLD) * KP
    print(f"rl: {refl_left} rr: {refl_right} s: {steering} b: {exit_var}")
    bob.drive(SPEED,-steering)
    
    if refl_right <= 15:
        exit_var += 1
    else:
        exit_var = 0
    if exit_var >= 10:
        break
#Waits for right sensor to see a black line
motor_left.hold()
motor_right.hold()

bob.settings(turn_rate=100)
bob.straight(50)
bob.turn(100)

while True:
    wait(1)
    refl_left = sensor.reflection()
    refl_right = sensor_2.reflection()
    steering = (refl_left - THRESHOLD) * KP
    print(f"rl: {refl_left} rr: {refl_right} s: {steering} b: {exit_var}")
    bob.drive(SPEED,-steering)
    
    if refl_right <= 15:
        exit_var += 1
    else:
        exit_var = 0
    if exit_var >= 10:
        break
