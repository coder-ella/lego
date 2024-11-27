from pybricks.hubs import InventorHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.tools import wait, StopWatch
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.robotics import DriveBase
from up import both_arms_up
from down import both_arms_down
from down1_up2 import left_down_right_up
from down2_up1 import left_up_right_down
import menu_code

#runs (in order), jurassic park theme, stop
arm_menu_options = ("M", "N", "O", "P", "X")
arm_num_options = len(arm_menu_options)
# Clear terminal
print("\x1b[H\x1b[2J", end="")

def two_menu(hub, bob, moyrorR, moyrorL):
    

    '''
    # default settings
    bob.settings(straight_speed=194, straight_acceleration=727
    ,turn_rate=221, turn_acceleration=995)
    '''
    selected = ""
    while True:
        # Based on the selection, choose a program.
        selected = menu_code.do_menu(hub,arm_menu_options,arm_num_options)
        if selected == "M":
            both_arms_up(hub,bob,moyrorR,moyrorL)
        elif selected == "N":
            both_arms_down(hub,bob,moyrorR,moyrorL)
        elif selected == "O":
            left_down_right_up(hub,bob,moyrorR,moyrorL)
        elif selected == "P":
            left_up_right_down(hub,bob,moyrorR,moyrorL)
        else:
            print("done with arm menu !")
            # this is the only way to stop PyBricks
            return 
    bob.stop()