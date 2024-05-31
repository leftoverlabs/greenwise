import time
import spidev
import RPi.GPIO as GPIO

# AD/DA channel on MCP3008
soil_channel = 0

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)


# Read SPI data from MCP3008, Channel must be an integer 0-7
def ReadADC(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data


# Calibration values 
min_moisture = 19200
max_moisture = 49300

readDelay = 0.5  # delay between readings

while True:
    # read moisture value and convert to percentage into the calibration range
    raw_data = ReadADC(soil_channel)
    moisture = (max_moisture - raw_data) * 100 / (max_moisture - min_moisture)

    # print values
    print("moisture: " + "%.2f" % moisture + "% (adc: " + str(raw_data) + ")")

    time.sleep(readDelay)  # set a delay between readings
