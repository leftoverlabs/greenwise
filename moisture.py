import time
import spidev
import RPi.GPIO as GPIO

# Configure Raspberry Pi
GPIO.setmode(GPIO.BCM)
soil_channel = 14
GPIO.setup(soil_channel, GPIO.IN)

# Calibration values 
min_moisture = 19200
max_moisture = 49300

readDelay = 0.5  # delay between readings

while True:
    # read moisture value and convert to percentage into the calibration range
    raw_data = GPIO.input(soil_channel)
    moisture = (max_moisture - raw_data) * 100 / (max_moisture - min_moisture)

    # print values
    print("moisture: " + "%.2f" % moisture + "% (adc: " + str(raw_data) + ")")

    time.sleep(readDelay)  # set a delay between readings
