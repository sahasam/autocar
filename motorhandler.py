import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
#Pin Constants

pinPWMA = 35 #control motor1 speed
pinAIN2 = 40 #motor1: direction 1
pinAIN1 = 38 #motor1: direction 2
pinSTBY = 37 #standby pin: must be set to high for motor to move
pinBIN1 = 31 #motor2: direction 1
pinBIN2 = 29 #motor2: direction 2
pinPWMB = 33 #control motor2 speed

#establish input and output pins
GPIO.setup(pinPWMA, GPIO.OUT) # Connected to PWMA
GPIO.setup(pinAIN2, GPIO.OUT) # Connected to AIN2
GPIO.setup(pinAIN1, GPIO.OUT) # Connected to AIN1
GPIO.setup(pinSTBY, GPIO.OUT) # Connected to STBY
GPIO.setup(pinBIN1, GPIO.OUT) # Connected to BIN1
GPIO.setup(pinBIN2, GPIO.OUT) # Connected to BIN2
GPIO.setup(pinPWMB, GPIO.OUT) # Connected to PWMB



#Motor functions: forward, backward, left, and right
def forwardDrive():
    GPIO.output(pinAIN1, GPIO.LOW)
    GPIO.output(pinAIN2, GPIO.HIGH)
    GPIO.output(pinSTBY, GPIO.HIGH)
    GPIO.output(pinPWMA, GPIO.HIGH)

def backwardDrive():
    GPIO.output(pinAIN2, GPIO.LOW)
    GPIO.output(pinAIN1, GPIO.HIGH)
    GPIO.output(pinSTBY, GPIO.HIGH)
    GPIO.output(pinPWMA, GPIO.HIGH)

def allstop():
    GPIO.output(pinAIN1, GPIO.LOW) # Set AIN1
    GPIO.output(pinAIN2, GPIO.LOW) # Set AIN2
    GPIO.output(pinPWMA, GPIO.LOW) # Set PWMA
    GPIO.output(pinSTBY, GPIO.LOW) # Set STBY
    GPIO.output(pinBIN1, GPIO.LOW) # Set BIN1
    GPIO.output(pinBIN2, GPIO.LOW) # Set BIN2
    GPIO.output(pinPWMB, GPIO.LOW) # Set PWMB

def turnLeft():
    GPIO.output(pinBIN1, GPIO.LOW)
    GPIO.output(pinBIN2, GPIO.HIGH)
    GPIO.output(pinSTBY, GPIO.HIGH)
    GPIO.output(pinPWMB, GPIO.HIGH)

def turnRight():
    GPIO.output(pinBIN2, GPIO.LOW)
    GPIO.output(pinBIN1, GPIO.HIGH)
    GPIO.output(pinSTBY, GPIO.HIGH)
    GPIO.output(pinPWMB, GPIO.HIGH)

