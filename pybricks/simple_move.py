from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#initialize robot parts
hub = PrimeHub()
motor_left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.D,Direction.CLOCKWISE)
motor_attach_left = Motor(Port.C, Direction.CLOCKWISE,gears=[20,12])
motor_attach_right = Motor(Port.B, Direction.CLOCKWISE,gears=[20,12])
sensor = ColorSensor(Port.F)
sensor_2 = ColorSensor(Port.E)
bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
wheel_diameter = 55.6, axle_track = 95)

#Go forward
bob.straight(500)
#Go backward
bob.straight(-500)
#Turn 90 degrees
bob.turn(90)
#Turn to other side
bob.turn(-180)
#Turn back to facing forward
bob.turn(90)
#Start attachment motors
motor_attach_left.run(900)
motor_attach_right.run(900)
wait(5000
#Move other direction
motor_attach_left.hold()
motor_attach_right.hold()
motor_attach_left.run(-900)
motor_attach_right.run(-900)
wait(5000)
#Stop attachment motors
motor_attach_left.hold()
motor_attach_right.hold()
