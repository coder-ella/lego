from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
import pybricks
from pybricks.parameters import Icon

#set robot parts
hub = InventorHub()
motor_left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.D,Direction.CLOCKWISE)
motor_attach_left = Motor(Port.C, Direction.CLOCKWISE,gears=[20,12])
motor_attach_right = Motor(Port.B, Direction.CLOCKWISE,gears=[20,12])
sensor = ColorSensor(Port.F)
sensor_2 = ColorSensor(Port.E)
bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
wheel_diameter = 55.6, axle_track = 95)

#Clear terminal and matrix
print("\x1b[H\x1b[2J", end="")
hub.display.off()

#set variables
voltage = hub.battery.voltage()
battery = 0
# https://github.com/rajrao/mypublicnotes/blob/master/Lego/PyBricks/notes.md
VMAX = 8300
VMIN = 6000

#write version and drivebase settings to terminal
print(f"version is{pybricks.version}")
print(f"settings are{bob.settings()}")

#Determine battery percentage
if voltage >= VMAX:
    print("battery is at 100%")
elif voltage <= VMIN:
    print("battery is at 1% or less")
else:
    battery = (voltage-VMIN)*100/(VMAX - VMIN)
    battery = round(battery)
    print(f"battery is at {(battery)}%, volts = {voltage}")

#change button color based on charge
if battery > 70:
    hub.light.on(Color.GREEN)
else:
    hub.light.on(Color.RED)

#display battery on matrix
if battery >= 20:
    hub.display.pixel(4,0)
if battery >= 40:
    hub.display.pixel(3,1)
    hub.display.pixel(4,1)
if battery >= 60:
    hub.display.pixel(2,2)
    hub.display.pixel(3,2)
    hub.display.pixel(4,2)
if battery >= 80:
    hub.display.pixel(1,3)
    hub.display.pixel(2,3)
    hub.display.pixel(3,3)
    hub.display.pixel(4,3)
if battery == 100:
    hub.display.pixel(0,4)
    hub.display.pixel(1,4)
    hub.display.pixel(2,4)
    hub.display.pixel(3,4)
    hub.display.pixel(4,4)

#wait 7 sec before changing display
wait(3000)
hub.display.off()
hub.display.number(battery)
wait(3000)
#show if battery life is sufficient
if battery > 70:
    hub.display.icon(Icon.HAPPY)
    hub.light.on(Color.GREEN)
else:
    hub.display.icon(Icon.SAD)
    hub.light.on(Color.RED)

#wait 4 sec in order to show icon before stopping code
wait(4000)
