import automationhat

humidity_adc_value = automationhat.analog.one.read()
print(humidity_adc_value)
