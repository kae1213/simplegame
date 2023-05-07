# way of using PySerial
import serial
import time

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
arduino.flush()

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

# Some things to do
# Whem Game receives a button press, for starters let it show as a print
while True:

# Whenever a interrupt is triggered, it will them get the pre-assigned int and then check if nonempty to print
    value_str = arduino.readline().decode('utf-8').rstrip()

    if(value_str):
        print("Received value:", value_str)
    
    