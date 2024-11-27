from pybricks.hubs import InventorHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.tools import wait, StopWatch
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.robotics import DriveBase


def do_menu(hub, menu_options, num_options):
    # menu_index is global, so that it can remember what the last menu-index was
    global menu_index
    menu_index=0
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