while True:
    adc_value = automationhat.analog.one.read()
    humidity_percentage = int(convert_to_humidity(humidity_adc_value))
    draw.rectangle((0, 0, WIDTH, HEIGHT), (0, 0, 0))  # Clear the screen
    draw.text((10, 10), f'Humidity: {humidity_percentage}%', fill=(255, 255, 255))
    disp.display(img)
    time.sleep(1)
