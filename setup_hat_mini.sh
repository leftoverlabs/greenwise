#!/bin/bash
# install_automation_hat.sh

# Define the installation directory
dir="~/automation-hat"

# Clone the repository into the defined directory
git clone https://github.com/pimoroni/automation-hat $dir

# Move into the cloned directory
cd $dir

# Run the installer
./install.sh

# Enable I2C and SPI buses
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_spi 0

# Add the activation command to bashrc file to create an alias
echo "alias activate_ah='source ~/.virtualenvs/pimoroni/bin/activate'" >> ~/.bashrc

# Add the deactivation command to bashrc to create an alias
echo "alias deactivate_ah='deactivate'" >> ~/.bashrc

# Use source command to apply changes immediately
source ~/.bashrc

echo "Installation complete. Use 'activate_automationhat' to activate the environment and 'deactivate_automationhat' to deactivate it."
