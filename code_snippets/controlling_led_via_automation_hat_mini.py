import time
import automationhat

time.sleep(0.1) # Pause for setup

while True:
    automationhat.output.one.write(1) # Turn on the LED
    time.sleep(1) # leave it on for a second
    automationhat.output.one.write(0) # Turn off the LED
    time.sleep(1) # leave it off for a second
