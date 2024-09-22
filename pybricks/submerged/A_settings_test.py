from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon       
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# https://docs.pybricks.com/en/latest/robotics.html

'''
# default settings
bob.settings(straight_speed=194, straight_acceleration=727
    ,turn_rate=221, turn_acceleration=995)

#max values allowed
bob.settings(straight_speed=970, straight_acceleration=9704
    ,turn_rate=1327, turn_acceleration=13271) 
# high speed
bob.settings(straight_speed=485, straight_acceleration=9704
    ,turn_rate=663, turn_acceleration=13271) 
'''

def settings_test():
    # Clear terminal
    print("\x1b[H\x1b[2J", end="")
    setting_names = ("straight_speed", "straight_acceleration","turn_rate","turn_acceleration")

    hub = InventorHub()
    motor_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
    motor_right = Motor(Port.D,Direction.CLOCKWISE)
    drivebase = DriveBase(left_motor = motor_left, right_motor=motor_right,
    wheel_diameter = 55.6, axle_track = 83.8)
    
    default_settings = drivebase.settings()
    print(default_settings)
    
    #settings found by testing different values until a ValueError: Invalid argument error was thrown
    drivebase.settings(straight_speed=970, straight_acceleration=9704,turn_rate=1327, turn_acceleration=13271)  
    #settings found by calling drivebase.settings() after the max values shown above
    drivebase.settings(straight_speed=485, straight_acceleration=9704,turn_rate=663, turn_acceleration=13271) 
    calc_max = (default_settings[0]/0.4, default_settings[0]/0.02,default_settings[2]/0.335, default_settings[2]/0.017)
    for i, s in enumerate(drivebase.settings()):
        print(f"{i} {setting_names[i]: <25}: {s: >5} multiple: {s/default_settings[i]: >7} calc max: {calc_max[i]: >5}")
        
    drivebase.settings(calc_max[0],calc_max[1],calc_max[2], calc_max[3])
    
    wait(200)
    drivebase.settings(straight_speed=970, straight_acceleration=9704,turn_rate=1327, turn_acceleration=13271)  
    drivebase.straight(1000)
   
    wait(200)
    drivebase.settings(straight_speed=485, straight_acceleration=9704,turn_rate=663, turn_acceleration=13271) 
    drivebase.straight(1000)
   
    wait(200)
    drivebase.settings(default_settings[0],default_settings[1],default_settings[2],default_settings[3])
    drivebase.straight(1000)

    if (False):
        # run motor test
        hub.speaker.beep()
        motor_right.run(100)
        wait(2000)
        hub.speaker.beep()
        motor_right.run(500)
        wait(2000)
        hub.speaker.beep()
        motor_right.run(750)
        wait(2000)
        hub.speaker.beep()
        motor_right.run(1000)
        wait(2000)
        hub.speaker.beep()
        motor_right.run(2000)
        wait(2000)
        hub.speaker.beep()
        motor_right.run(3000)
        wait(2000)
        motor_right.stop()
    
    print("done")


if __name__ == '__main__':
    settings_test()