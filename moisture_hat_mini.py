import time
import automationhat


# Adjust this function to convert the analog reading (0.0 to 1.0)
# to a humidity reading (0% to 100%), based on the humidity sensor's datasheet
def convert_to_humidity(analog_value):
    return analog_value * 100.0


while True:
    # Read the value from ADC 1, returns a value between 0.0 and 1.0
    adc_value = automationhat.analog.one.read()
    # Convert this into a humidity reading
    humidity = convert_to_humidity(adc_value)

    print(f'The humidity level is: {humidity}%')

    # Update display on the Automation HAT
    automationhat.display.oled.write(f"Humidity: {humidity:2.2f}%")
    automationhat.display.oled.show()

    # Wait for a while before the next reading, no need to read the sensor continuously
    time.sleep(1)
