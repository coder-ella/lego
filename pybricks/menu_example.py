from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.tools import wait

menu_options = ("F", "L", "R", "B", "Q") #forward, left, right, back
num_options = len(menu_options)
hub = PrimeHub()

def do_menu(hub):
    # Normally, the center button stops the program. But we want to use the
    # center button for our menu. So we can disable the stop button.

    hub.system.set_stop_button(None)
    menu_index = 0
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
    if selected == "F":
        # you could import another file here by using
        # import drive_forward
        # or use a function! here we are writing the code in-line
        print("driving foward")
    elif selected == "L":
        print("turning left")
    elif selected == "R":
        print("turning right")
    elif selected == "B":
        print("driving forward")
    else:
        print("done!")
