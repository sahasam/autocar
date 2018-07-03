import RPi.GPIO as GPIO
import time

'''
This program is much simpler than using the capacitors to fill up.

It takes advantage that 0 and 1 are determined by voltages, so I use a voltage
divider with a potentiometer so I can tune the threshold. It is much faster than 
counting time to discharge. All it does is poll the input pin and it returns 1 or 0

In addition, use this code to tune potentiometer for different brightnesses
'''

#initialize variables
circuit_pin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(circuit_pin, GPIO.IN)

try:
    while True: 
        #all it does is print the input for circuit pin
        print(GPIO.input(circuit_pin))
        time.sleep(0.001)
except KeyboardInterrupt:
    GPIO.cleanup()
