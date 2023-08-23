from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Icon

#Clear terminal
print("\x1b[H\x1b[2J", end="")

hub = InventorHub()

voltage = hub.battery.voltage()
battery = 0
VMAX = 8300
VMIN = 6000

if voltage >= VMAX:
    print("battery is at 100%")
    battery = 100
elif voltage <= VMIN:
    print("battery is at 1% or less")
else:
    battery = round((voltage-VMIN)*100/(VMAX - VMIN))
    print(f"battery is at {battery}%, volts = {voltage}")

hub.display.off()
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


wait(7000)
#hub.display.icon(Icon.HAPPY)
#wait(2000)

if battery > 70:
    hub.display.icon(Icon.HAPPY)
else:
    hub.display.icon(Icon.SAD)
wait(4000)