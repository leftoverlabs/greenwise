#!/bin/bash

# define location where the virtual environment will be created
PROJECT_DIR=~/greenwise

# Update package list
# sudo apt-get update
# Enable SPI
sudo raspi-config nonint do_spi 0

# Enable I2C
sudo raspi-config nonint do_i2c 0

# Install python3 virtualenv if needed
if ! command -v virtualenv >/dev/null; then
    echo "virtualenv not found. Installing virtualenv..."
    sudo apt-get install -y python3-virtualenv
fi

# Install virtualenvwrapper if needed
if ! command -v virtualenvwrapper >/dev/null; then
    echo "virtualenvwrapper not found. Installing virtualenvwrapper..."
    sudo apt-get install -y virtualenvwrapper
fi

# Source the virtualenvwrapper script and set environment variables
if ! grep -q 'export WORKON_HOME=~/.virtualenvs' ~/.bashrc ; then
	echo 'export WORKON_HOME=~/.virtualenvs' >> ~/.bashrc
fi

VIRTUALENVWRAPPER_PYTHON=$(which python3)
if ! grep -q "export VIRTUALENVWRAPPER_PYTHON=$VIRTUALENVWRAPPER_PYTHON" ~/.bashrc ; then
	 echo "export VIRTUALENVWRAPPER_PYTHON=$VIRTUALENVWRAPPER_PYTHON" >> ~/.bashrc
fi

if ! grep -q 'source /usr/share/virtualenvwrapper/virtualenvwrapper.sh' ~/.bashrc ; then
	echo 'source /usr/share/virtualenvwrapper/virtualenvwrapper.sh' >> ~/.bashrc
fi

# reload .bashrc so that changes take effect in the current session
source ~/.bashrc

# Create a new virtual environment named greenwise
mkvirtualenv -p $VIRTUALENVWRAPPER_PYTHON greenwise -a ~/greenwise

workon greenwise

pip install pillow
pip install automationhat
pip install st7735

echo "You can now activate the greenwise environment using 'workon greenwise'. To deactivate, use 'deactivate'."
