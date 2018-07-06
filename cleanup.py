'''
sometimes when the program doesn't end correctly, the motors and other GPIO ports may
still be in use

run 'make clean' in terminal to run this and other necessary cleaning functions
'''
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
#motorhandler pins
pinPWMA = 35 #control motor1 speed
pinAIN2 = 40 #motor1: direction 1
pinAIN1 = 38 #motor1: direction 2
pinSTBY = 37 #standby pin: must be set to high for motor to move
pinBIN1 = 31 #motor2: direction 1
pinBIN2 = 29 #motor2: direction 2
pinPWMB = 33 #control motor2 speed
GPIO.setup(pinPWMA, GPIO.OUT) # Connected to PWMA
GPIO.setup(pinAIN2, GPIO.OUT) # Connected to AIN2
GPIO.setup(pinAIN1, GPIO.OUT) # Connected to AIN1
GPIO.setup(pinSTBY, GPIO.OUT) # Connected to STBY
GPIO.setup(pinBIN1, GPIO.OUT) # Connected to BIN1
GPIO.setup(pinBIN2, GPIO.OUT) # Connected to BIN2
GPIO.setup(pinPWMB, GPIO.OUT) # Connected to PWMB
#ldr pins
GPIO.setup(7,GPIO.OUT)

GPIO.cleanup()
