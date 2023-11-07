from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
import pybricks
from pybricks.parameters import Icon

def run_diagnostics(hub):
    #Clear terminal and matrix
    print("\x1b[H\x1b[2J", end="")
    hub.display.off()

    #set variables
    voltage = hub.battery.voltage()
    battery = 0
    # https://github.com/rajrao/mypublicnotes/blob/master/Lego/PyBricks/notes.md
    VMAX = 8300
    VMIN = 6000

    #write version to terminal
    print(f"version is{pybricks.version}")
    
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

    wait(1500)
    hub.display.off()
    hub.display.number(battery)
    wait(1500)
    #show if battery life is sufficient
    if battery > 70:
        hub.display.icon(Icon.HAPPY)
        hub.light.on(Color.GREEN)
    else:
        hub.display.icon(Icon.SAD)
        hub.light.on(Color.RED)

    #wait 4 sec in order to show icon before stopping code
    wait(1000)
    hub.light.on(Color.BLUE)

if __name__ == '__main__':
    print("testing")
    hub = InventorHub()
    run_diagnostics(hub)