#!/bin/bash

# Clone the repository
git clone https://github.com/pimoroni/automation-hat

# Move into the cloned directory
cd automation-hat

# Run the installer
./install.sh

# Enable I2C and SPI buses
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_spi 0

# Add the activation command to bashrc file to create an alias
echo "alias activate_automationhat='source ~/.virtualenvs/pimoroni/bin/activate'" >> ~/.bashrc

# Add the deactivation command to bashrc to create an alias
echo "alias deactivate_automationhat='deactivate'" >> ~/.bashrc

# Use source command to apply changes immediately
source ~/.bashrc

echo "Installation complete. Use 'activate_automationhat' to activate the environment and 'deactivate_automationhat' to deactivate it."
