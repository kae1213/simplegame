import serial
import time
#CHECK THIS OUT MAY HELP
#link: https://forum.arduino.cc/t/reading-an-int-value-from-arduino-with-pyserial/92776

left_button_pressed = False
right_button_pressed = False

def button_state(value_hold):
    if (value_hold == '0'):
        print("Received value:", value_hold)
        #left_button_pressed = True
        return True, False

    elif (value_hold == '1'):
        print("Received value:", value_hold)
        return False, True

    else:
        print("Invalid")

def connect_to_controller():
    arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
    arduino.flush()
    return arduino

def get_controller_inputs(arduino):
    value_str = arduino.readline().decode('utf-8').rstrip()
    if (value_str):
        button_state(value_str)

def enable_controller():#will not use, this will stay stuck checking while loop, but first iteration
    arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
    arduino.flush()
    
    while True:
    # Whenever a interrupt is triggered, it will them get the pre-assigned int and then check if nonempty to print
        value_str = arduino.readline().decode('utf-8').rstrip()
        if (value_str):
            button_state(value_str)