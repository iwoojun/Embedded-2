#!/usr/bin/python3
"""
Names: In Woo Jun
Student Number: JNXINW001
Prac: Prac1
Date: 23/07/2019
"""
# import Relevant Librares
import time #import time library
import RPi.GPIO as GPIO #import raspberry pi GPIO library

GPIO.setwarnings(False) #prevent run time warning that channel is already in use

#setting GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) #set LED1
GPIO.setup(23, GPIO.OUT) #set LED2
GPIO.setup(24, GPIO.OUT) #set LED3
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #set SWITCH1 and initial value to be pulled down
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #set SWITCH2 and initial value to be pulled down

def LED1on(): #function to turn on LED1
    GPIO.output(18, True)
    time.sleep(0.01)

def LED1off(): #function to turn off LED1
    GPIO.output(18, False)
    time.sleep(0.01)

def LED2on(): #function to turn on LED2
    GPIO.output(23, True)
    time.sleep(0.01)

def LED2off(): #function to turn off LED2
    GPIO.output(23, False)
    time.sleep(0.01)

def LED3on(): #function to turn on LED3
    GPIO.output(24, True)
    time.sleep(0.01)

def LED3off(): #function to turn off LED3
    GPIO.output(24, False)
    time.sleep(0.01)

LEDcounter = 0 #create variable LEDcounter
str_bin_conv = 0 #create variable str_bin_conv

def switch1_callback(channel): #function when switch1 (increment) is pressed
    global LEDcounter
    global str_bin_conv
    if LEDcounter < 7: #increment by 1 until LEDcounter reaches 7
        LEDcounter += 1
    else:
        LEDcounter = 0 #when LEDcounter reaches its maximum, restart at 0
    bin_conv = bin(LEDcounter)[2:].zfill(3) #convert LEDcounter to binary, then cut off the "0b" by slicing, and then fill the number by keeping it 3 digits
    str_bin_conv = str(bin_conv) #convert bin_conv to string

    if str_bin_conv[:1] == "1": #check if first digit is 1, if true then turn on LED 1
        LED1on()
    else: #if not, turn off LED 1
        LED1off()

    if str_bin_conv[1:2] == "1": #check if first digit is 1, if true then turn on LED 2
        LED2on()
    else: #if not, turn off LED 2
        LED2off()

    if str_bin_conv[2:3] == "1": #check if first digit is 1, if true then turn on LED 3
        LED3on()
    else: #if not, turn off LED 3
        LED3off()

def switch2_callback(channel): #function when switch2 (decrement) is pressed
    global LEDcounter
    global str_bin_conv
    if LEDcounter > 0: #decrement by 1 until LEDcounter reaches 0
        LEDcounter -=1
    else: #when LEDcounter reaches its minimum, restart at 7
        LEDcounter = 7
    bin_conv = bin(LEDcounter)[2:].zfill(3) #convert LEDcounter to binary, then cut off the "0b" by slicing, and then fill the number by keeping it 3 digits
    str_bin_conv = str(bin_conv) #convert bin_conv to string

    if str_bin_conv[:1] == "1": #check if first digit is 1, if true then turn on LED 1
        LED1on()
    else: #if not, turn off LED 1
        LED1off()

    if str_bin_conv[1:2] == "1": #check if first digit is 1, if true then turn on LED 2
        LED2on()
    else: #if not, turn off LED 2
        LED2off()

    if str_bin_conv[2:3] == "1": #check if first digit is 1, if true then turn on LED 3
        LED3on()
    else: #if not, turn off LED 3
        LED3off()


GPIO.add_event_detect(17, GPIO.RISING, callback=switch1_callback, bouncetime=300) #setup event when SWITCH1 rises
GPIO.add_event_detect(27, GPIO.RISING, callback=switch2_callback, bouncetime=300) #setup event when SWITCH2 rises

#main function
def main():
    switch1 = input("Press switch 1 to increment\nPress switch 2 to decrement\n")
    GPIO.cleanup() #clean up and reset GPIO ports

# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
