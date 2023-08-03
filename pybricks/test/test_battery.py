from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#Clear terminal
print("\x1b[H\x1b[2J", end="")

hub = InventorHub()

voltage = hub.battery.voltage()
battery = 0
VMAX = 8300
VMIN = 6000

if voltage >= VMAX:
    print("battery is at 100%")
elif voltage <= VMIN:
    print("battery is at 1% or less")
else:
    battery = (voltage-VMIN)*100/(VMAX - VMIN)
    print(f"battery is at {round(battery)}%, volts = {voltage}")

