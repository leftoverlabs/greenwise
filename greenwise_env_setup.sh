#!/bin/bash

# Define location where the virtual environment will be created
PROJECT_DIR=~/greenwise
mkdir $PROJECT_DIR

# Update package list
sudo apt-get update

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
if ! command -v virtualenvwrapper.sh >/dev/null; then
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

# Reload .bashrc so that changes take effect in the current session
source ~/.bashrc

# Debug print statements to check if paths are set correctly
echo "WORKON_HOME is set to $WORKON_HOME"
echo "VIRTUALENVWRAPPER_PYTHON is set to $VIRTUALENVWRAPPER_PYTHON"
echo "virtualenvwrapper.sh is sourced"

# Source the virtualenvwrapper script directly to ensure it's available
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh

# Create a new virtual environment named greenwise
mkvirtualenv greenwise -a "$PROJECT_DIR" -p "$VIRTUALENVWRAPPER_PYTHON"

# Workon new virtual environment
workon greenwise

# Install necessary packages
pip install pillow automationhat st7735

echo "You can now activate the greenwise environment using 'workon greenwise'. To deactivate, use 'deactivate'."
