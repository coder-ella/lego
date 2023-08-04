from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#Clear terminal
print("\x1b[H\x1b[2J", end="")

#initialize hub, motors, sensors, drivebase
hub = InventorHub()
motor_left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.D,Direction.CLOCKWISE)
motor_attach_left = Motor(Port.C, Direction.CLOCKWISE,gears=[20,12])
motor_attach_right = Motor(Port.B, Direction.CLOCKWISE,gears=[20,12])
sensor = ColorSensor(Port.F)
sensor_2 = ColorSensor(Port.E)
bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
wheel_diameter = 55.6, axle_track = 95)

#Minimum reflection to turn, 55 is between white and black
THRESHOLD = 55
#Line follow speed
SPEED = 140
#Constant of proportionality for moving
KP = 1
#How many times right color sensor has seen black in a row
exit_var = 0
#55, 0.25 - 43, 0.25 work for THRESHOLD, SPEED, and KP 
#Set settings
bob.settings(straight_speed=100,
straight_acceleration=100)

#Go to the line from home base
bob.straight(50)

while True:
    wait(1)
    refl_left = sensor.reflection()
    refl_right = sensor_2.reflection()
    steering = (refl_left - THRESHOLD) * KP
    print(f"rl: {refl_left} rr: {refl_right} s: {steering} b: {exit_var}")
    bob.drive(SPEED,-steering)
    
    #<= 15 is black
    if refl_right <= 15:
        exit_var += 1
    else:
        exit_var = 0
    #Takes sensor 10 times of seeing black for back line to pass.
    if exit_var >= 10:
        break
#Waits for right sensor to see a black line
motor_left.hold()
motor_right.hold()

#Change turn speed
bob.settings(turn_rate=100)
#Go past line
bob.straight(50)
#Turn toward other line
bob.turn(100)

#Follow next line
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
