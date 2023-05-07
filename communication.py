# way of using PySerial
import serial
import time

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
arduino.flush()

def button_state(value):
    match value:
        case '100':
            print("Received value:", value)
        case '111':
            print("Received value:", value)
        case _:
            print("Invaliud")

while True:

# Whenever a interrupt is triggered, it will them get the pre-assigned int and then check if nonempty to print
    value_str = arduino.readline().decode('utf-8').rstrip()
    if (value_str):
        button_state(value_str)
    
