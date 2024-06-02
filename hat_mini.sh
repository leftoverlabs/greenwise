# Update the package lists and upgrade existing packages
sudo apt-get update && sudo apt-get upgrade -y

# Install the Automation HAT library
curl https://get.pimoroni.com/automationhat | bash

# Reboot the system
sudo reboot
