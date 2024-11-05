from pybricks.hubs import InventorHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.tools import wait, StopWatch
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.robotics import DriveBase

from A_fn_diagnostics import run_diagnostics
from A_clean_wheels import clean

from item_collection_test_run_cablooie_2 import item_collection
from m_09_m_o_2024_09_15_v2 import m_09
from m_09_m_o_2024_09_15_v2_p2 import m_09_p2
from m_11_2024_10_11 import kelp_mission
from m_trident import m_10
from z_jurasic_park import jurasic_park_theme



hub = InventorHub()
motor_left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.A,Direction.CLOCKWISE)
moyrorR = Motor(Port.F)
moyrorL = Motor(Port.E)
bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
wheel_diameter = 55.6, axle_track = 83.79999999999997)

#runs (in order), jurassic park theme, stop
menu_options = ("1", "2", "3", "4", "5", "J", "C", "D", "X")
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
            hub.speaker.beep()
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


'''
# default settings
bob.settings(straight_speed=194, straight_acceleration=727
    ,turn_rate=221, turn_acceleration=995)
'''
selected = ""
while True:
    # Based on the selection, choose a program.
    selected = do_menu(hub)
    if selected == "1":
        item_collection(hub,bob,moyrorR,moyrorL)
    elif selected == "2":
        kelp_mission(hub,bob,moyrorR,moyrorL)
    elif selected == "3":
        m_09(hub,bob,moyrorR,moyrorL)
    elif selected == "4":
        m_09_p2(hub,bob,moyrorR,moyrorL)
    elif selected == "5":
        m_10(hub,bob,moyrorR,moyrorL)
    elif selected == "J":
        jurasic_park_theme(hub,bob,moyrorR,moyrorL)
    elif selected == "C":
        clean(hub,bob)
    elif selected == "D":
        run_diagnostics(hub)
    else:
        print("done!")
        # this is the only way to stop PyBricks
        raise SystemExit("Closing program..")
    bob.stop()