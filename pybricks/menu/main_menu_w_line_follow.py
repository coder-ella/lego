from pybricks.hubs import InventorHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.tools import wait, StopWatch
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.robotics import DriveBase

from fn_diagnostics import run_diagnostics
from fn_test import *
from simple_test import simple_move
from fn_cargo_connect_line_follow import *

hub = InventorHub()
motor_left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.D,Direction.CLOCKWISE)
motor_attach_left = Motor(Port.C, Direction.CLOCKWISE,gears=[20,12])
motor_attach_right = Motor(Port.B, Direction.CLOCKWISE,gears=[20,12])
sensor = ColorSensor(Port.F)
sensor_2 = ColorSensor(Port.E)
bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
wheel_diameter = 55.6, axle_track = 95)

menu_options = ("1", "M", "D","X") #forward, left, right, back, exit
menu_index = 0
num_options = len(menu_options)

# Clear terminal
print("\x1b[H\x1b[2J", end="")

def do_menu(hub):
    # Normally, the center button stops the program. But we want to use the
    # center button for our menu. So we can disable the stop button.
    global menu_index
    hub.system.set_stop_button(None)
    while True:
        hub.display.char(menu_options[menu_index])
        # Wait for any button.
        pressed = ()
        while not pressed:
            pressed = hub.buttons.pressed()
            wait(10)    
        print(f"pressed: {pressed}")
        # and then wait for the button to be released.
        while hub.buttons.pressed():
            wait(10)
  
        # Now check which button was pressed.
        if Button.CENTER in pressed:
            # Center button, this is the selection button, so we can exit the
            # selection loop
            break
        elif Button.LEFT in pressed:
            # Left button, so decrement menu menu_index.
            menu_index -= 1
            if (menu_index < 0): #roll over!
                menu_index = num_options - 1
        elif Button.RIGHT in pressed:
            # Right button, so increment menu menu_index.
            menu_index += 1
            if (menu_index >= num_options):
                menu_index = 0
        print(f"menu_index:{menu_index}")
    
    # Now we want to use the Center button as the stop button again.
    hub.system.set_stop_button(Button.CENTER)
    selected = menu_options[menu_index]
    print(f"menu option selected {selected}")
    
    return selected

selected = ""
while True:
    # Based on the selection, choose a program.
    selected = do_menu(hub)
    if selected == "1":
        print("line_follow_3")
        line_follow_3(hub, motor_left, motor_right, motor_attach_right, 
        motor_attach_left, sensor, sensor_2, bob)
        bob.stop()
    elif selected == "M":
        print("Simple move")
        simple_move(hub, bob, motor_attach_left, motor_attach_right)
        bob.stop()
    elif selected == "D":
        print(f"bob's settings are{bob.settings()}")
        run_diagnostics(hub)
        bob.stop()
    else:
        print("done!")
        raise SystemExit("Closing program..")

