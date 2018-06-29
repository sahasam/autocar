import logging
import sys
import time

#import the BNO055 Sensor API
from Adafruit_BNO055 import BNO055

#initialize the Gyroscope Object
bno = BNO055.BNO055(serial_port='/dev/serial0', rst=18)

#Allow verbose logging abilities
if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
    loggin.basicConfig(level=logging.DEBUG)

#establish connection to BNO055. For more information on how to connect, check the readMe
if not bno.begin():
    raise RuntimeError('Failed to initialize BNO055. Check connection. Did you set up serial properly')

#print status.
status, self_test, error = bno.get_system_status()
print('System status: {0}'.format(status))
print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))

try:
    while True:
        #get heading from bno055. You have to get the rest of the values to satisfy the function
        heading, roll, pitch = bno.read_euler()
        print('heading: {0:0.3F}'.format(heading))
        time.sleep(0.05)
except KeyboardInterrupt: 
    print('\nprogram finished')
