import time
import ldrhandler
import motorhandler
import bnohandler

try:
    while True:
        motorhandler.forwardDrive()
        print(bnohandler.getHeading())
        time.sleep(0.01)
except  KeyboardInterrupt:
    motorhandler.GPIO.cleanup()
    ldrhandler.cleanup()
