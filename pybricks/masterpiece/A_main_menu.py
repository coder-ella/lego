from pybricks.hubs import InventorHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.tools import wait, StopWatch
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.robotics import DriveBase

from A_fn_diagnostics import run_diagnostics
from A_joe import Everett_Grace_Function
from A_Light_Show_Mission_Current import *
from A_clean_wheels import *
from A_dragon_joe import *
from A_stage import *

hub = InventorHub()
motor_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.D,Direction.CLOCKWISE)
motor_attach_left = Motor(Port.A)
motor_attach_right = Motor(Port.B)
#sensor = ColorSensor(Port.F)
#sensor_2 = ColorSensor(Port.E)
bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
wheel_diameter = 55.6, axle_track = 83.79999999699997)

menu_options = ("1", "2", "3","4","5","6", "D", "C", "X") #forward, left, right, back, exit
menu_index = 0
num_options = len(menu_options)

# Clear terminal
print("\x1b[H\x1b[2J", end="")

def do_menu(hub):
    # menu_index is global, so that it can remember what the last menu-index was
    global menu_index
    # Normally, the center button stops the program. But we want to use the
    # center button for our menu. So we can disable the stop button.
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
            print(f"Selected Index: {menu_index}")
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
        light_show_run(hub, bob, motor_attach_right)
    elif selected == "3":
        Everett_Grace_Function(hub, bob, motor_attach_left)
    elif selected == "4":
        dragon_run(hub, bob, motor_attach_left)
    elif selected == "5":
        run_theater(hub, bob, motor_attach_left,2)
    elif selected == "6":
        run_theater(hub, bob, motor_attach_left,3)
    elif selected == "D":
        print(f"bob's settings are{bob.settings()}")
        run_diagnostics(hub)
    elif selected == "C":
        clean(hub, bob)
        
    else:
        print("done!")
        # this is the only way to stop PyBricks
        raise SystemExit("Closing program..")
    bob.stop()
