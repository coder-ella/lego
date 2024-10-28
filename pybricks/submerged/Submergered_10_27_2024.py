from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon       
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from item_collection_test_run_cablooie_2 import item_collection
from m_11_2024_10_11 import kelp_mission
from m_09_m_o_2024_09_15_v2 import m_09
from m_trident import m_10
from z_jurasic_park import jurasic_park_theme



if __name__ == '__main__':
    print(__name__)
    hub = InventorHub()
    motor_left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
    motor_right = Motor(Port.A,Direction.CLOCKWISE)
    moyrorR = Motor(Port.F)
    moyrorL = Motor(Port.E)
    bob = DriveBase(left_motor = motor_left, right_motor=motor_right,
    wheel_diameter = 55.6, axle_track = 83.79999999999997)

    # Wait for any button.
    pressed = ()
    while not pressed:
        pressed = hub.buttons.pressed()
        wait(10)
    hub.speaker.beep()
    item_collection(hub,bob,moyrorR,moyrorL)

    pressed = ()
    while not pressed:
        pressed = hub.buttons.pressed()
        wait(10)
    hub.speaker.beep()
    kelp_mission(hub,bob,moyrorR,moyrorL)

    pressed = ()
    while not pressed:
        pressed = hub.buttons.pressed()
        wait(10)
    hub.speaker.beep()
    m_09(hub,bob,moyrorR,moyrorL)

    pressed = ()
    while not pressed:
        pressed = hub.buttons.pressed()
        wait(10)
    hub.speaker.beep()
    m_10(hub,bob,moyrorR,moyrorL)
    print("Submerged 2024 Complete")
    jurasic_park_theme(hub,bob,moyrorR,moyrorL)
