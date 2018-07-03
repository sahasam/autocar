import time
import ldrhandler

try:
    while True:
        print('working')
        time.sleep(1)
except  KeyboardInterrupt:
    motorhandler.GPIO.cleanup()
    ldrhandler.cleanup()
