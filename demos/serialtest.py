import serial
import time

ser = serial.Serial('/dev/serial0', 9600, timeout = 1.0, rtscts = 0)

while True:
    ser.write('hello')
    read = ser.read(5)
    print read
    time.sleep(1)
