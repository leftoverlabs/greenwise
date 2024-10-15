def convert_to_humidity(analog_value):
    min_value = 1.05 
    max_value = 2.09 
    return 100 - ((analog_value - min_value) / (max_value - min_value)) * 100.0

humidity_percentage = int(convert_to_humidity(humidity_adc_value))
