from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import vector, wait, StopWatch

print("\x1b[H\x1b[2J", end="")
wait(5)

SPEED = 0
KP = 10
KI = 1.0
KD = 0.5
hub = InventorHub(top_side=vector(1,0,0), front_side=vector(0,1,0))
motor_left = Motor(Port.F, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.B,Direction.CLOCKWISE)
exit_var = 0
start_angle = hub.imu.rotation(Axis.Y)
i = 0
prev_error = 0
hub.speaker.beep()
watch = StopWatch()

while True:
    angle_y = hub.imu.rotation(Axis.Y)
    error = (start_angle - angle_y)
    p = error * KP
    i = KI * (error + i) 
    d = KD * (error - prev_error)
    move = p + i + d
    motor_left.dc(move+SPEED)
    motor_right.dc(move+SPEED)
    print(f"{error},{move},{move + SPEED},{start_angle}")
    prev_error = error
    wait(2)
    if watch.time() >= 25000:
        hub.speaker.beep()
        break


motor_left.hold()
motor_right.hold()
