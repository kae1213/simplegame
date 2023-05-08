# way of using PySerial
import serial
import time
#CHECK THIS OUT MAY HELP
#link: https://forum.arduino.cc/t/reading-an-int-value-from-arduino-with-pyserial/92776

left_button_pressed = False
right_button_pressed = False

# arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
# arduino.flush()

def button_state(value_hold, left_button_pressed, right_button_pressed):
    if (value_hold == "100"):
        print("Received value:", value_hold)
        left_button_pressed = True

    elif (value_hold == "111"):
        print("Received value:", value_hold)
        right_button_pressed = True

    else:
        print("Invalid")

def return_button_state(button_state):
    button_state = False

#while True:

# Whenever a interrupt is triggered, it will them get the pre-assigned int and then check if nonempty to print
    # value_str = arduino.readline().decode('utf-8').rstrip()
    # if (value_str):
    #     button_state(value_str)
    


def connect_to_controller():
    arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
    arduino.flush()
    return arduino

def get_controller_inputs(arduino):
    value_str = arduino.readline().decode('utf-8').rstrip()
    if (value_str):
        button_state(value_str)

def enable_controller():#will not use, this will stay stuck checking while loop
    arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
    arduino.flush()
    
    while True:

# Whenever a interrupt is triggered, it will them get the pre-assigned int and then check if nonempty to print
        value_str = arduino.readline().decode('utf-8').rstrip()
        if (value_str):
            button_state(value_str)