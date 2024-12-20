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
from m_trident_shark import m_10
from m_trident import m_10_1
from z_jurasic_park import jurasic_park_theme
from sample_return import boat_return
from A_main_menu_arms import two_menu
import menu_code
from m_mast_lift import mast_lift

hub = InventorHub()
motor_left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.A,Direction.CLOCKWISE)
moyrorR = Motor(Port.F)
moyrorL = Motor(Port.E)
bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
wheel_diameter = 55.6, axle_track = 83.79999999999997)

#runs (in order), jurassic park theme, stop
main_menu_options = ("1", "2", "3", "4", "5", "6", "7", "8", "J", "C", "D", "A", "X")
num_options = len(main_menu_options)


# Clear terminal
print("\x1b[H\x1b[2J", end="")

hub.speaker.beep()
'''
hub.speaker.play_notes(notes = [
        "D3/8", "C#3/8", "D3/4", "A2/4", "G2/4", 
        ],tempo=220)
'''
'''
# default settings
bob.settings(straight_speed=194, straight_acceleration=727
    ,turn_rate=221, turn_acceleration=995)
'''
selected = ""
menu_code.menu_index = 0
while True:
    # Based on the selection, choose a program.
    selected = menu_code.do_menu(hub,main_menu_options, num_options)
    if selected == "1":
        item_collection(hub,bob,moyrorR,moyrorL)
        menu_code.menu_index = 1
    elif selected == "2":
        kelp_mission(hub,bob,moyrorR,moyrorL)
        menu_code.menu_index = 2
    elif selected == "3":
        m_09(hub,bob,moyrorR,moyrorL)
        menu_code.menu_index = 3
    elif selected == "4":
        m_09_p2(hub,bob,moyrorR,moyrorL)
        menu_code.menu_index = 4
    elif selected == "5":
        m_10(hub,bob,moyrorR,moyrorL)
        menu_code.menu_index = 5
    elif selected == "6":
        mast_lift(hub, bob, moyrorR, moyrorL)
        menu_code.menu_index = 6
    elif selected == "7":
        boat_return(hub,bob,moyrorR,moyrorL)
        menu_code.menu_index = 7
    elif selected == "8":
        m_10_1(hub,bob,moyrorR,moyrorL)
    elif selected == "J":
        jurasic_park_theme(hub,bob,moyrorR,moyrorL)
    elif selected == "C":
        clean(hub,bob)
    elif selected == "D":
        run_diagnostics(hub)
    elif selected == "A":
        two_menu(hub, bob, moyrorR, moyrorL)
    else:
        print("done!")
        # this is the only way to stop PyBricks
        raise SystemExit("Closing program..")
    bob.stop()