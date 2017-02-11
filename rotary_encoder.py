import CHIP_IO.GPIO as GPIO
import time
 


PIN_A = "XIO-P0"
PIN_B = "XIO-P1"


GPIO.setup(PIN_A, GPIO.IN)
GPIO.setup(PIN_B, GPIO.IN)

counter = 0
clkLastState = GPIO.input(PIN_A)

try:

        while True:
                clkState = GPIO.input(PIN_A)
                dtState = GPIO.input(PIN_B)
                if clkState != clkLastState:
                        if dtState != clkState:
                                counter += 1
                        else:
                                counter -= 1
                        print counter
                clkLastState = clkState
finally:
        GPIO.cleanup()

