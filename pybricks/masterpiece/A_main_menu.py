from pybricks.hubs import InventorHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.tools import wait, StopWatch
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.robotics import DriveBase

from A_fn_diagnostics import run_diagnostics
from A_joe import *
from A_Light_Show_Mission_V5 import *
from A_Long_Poker_Thing_V2 import *
from A_clean_wheels import *
from A_dragon_joe import *
from A_stizzy import *
from A_daddy_dropoff import *
from A_Camera import *

hub = InventorHub()
motor_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.D,Direction.CLOCKWISE)
motor_attach_left = Motor(Port.A)
motor_attach_right = Motor(Port.B)
#sensor = ColorSensor(Port.F)
#sensor_2 = ColorSensor(Port.E)
bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
wheel_diameter = 55.6, axle_track = 83.79999999699997)
default_settings = bob.settings()

menu_options = ("1", "2", "3","4","5","6", "7", "D", "C") #forward, left, right, back, exit
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

        if Button.BLUETOOTH in pressed:
            # This is the exit key!
            return "X"
  
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

if hub.imu.ready():
    print("IMU is ready")
    hub.display.icon(Icon.HEART)
else:
    print("IMU is NOT ready!")
    hub.speaker.play_notes(["C3/4","D3/4","C2/2"])
    hub.display.icon(Icon.FALSE)

'''
# highs 
straight_speed=485, straight_acceleration=9704
turn_rate=663, turn_acceleration=13271) 
'''
selected = ""
while True:
    try:
        # Based on the selection, choose a program.
        selected = do_menu(hub)
        bob.settings(default_settings[0],default_settings[1],
        default_settings[2],default_settings[3])
        if selected == "1":
            longy(hub, bob, motor_attach_right)
        elif selected == "2":
            light_show_run(hub, bob, motor_attach_right, motor_attach_left)
        elif selected == "3":
            Everett_Grace_Function(hub, bob, motor_attach_left)
        elif selected == "4":
            dragon_run(hub, bob, motor_attach_left)
        elif selected == "5":
            camera_run(hub, bob, motor_attach_left)  
        elif selected == "6":
            run_theater(hub, bob, motor_attach_left,2)
        elif selected == "7":
            run_theater(hub, bob, motor_attach_left,3)
             
        elif selected == "D":
            print(f"bob's settings are{bob.settings()}")
            run_diagnostics(hub)
        elif selected == "C":
            clean(hub, bob)
        else:
            print(f"don't know selected value {selected}")
            selected = "X"
            # this is the only way to stop PyBricks
            raise SystemExit("Closing program..")
    except SystemExit:
        if selected == "X":
            raise SystemExit()
        bob.stop()
        motor_left.stop()
        motor_right.stop()
        hub.speaker.beep(frequency=1, duration = 50)
        while hub.buttons.pressed():
            wait(100) # wait for button to be released

    bob.stop()