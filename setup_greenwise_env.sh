#!/bin/bash

# Update package list
sudo apt-get update

# Check whether virtualenv module is installed
virtualenv --version &>/dev/null
if [ $? -ne 0 ]; then
    echo "virtualenv not found. Installing virtualenv..."
    sudo apt-get install -y python3-virtualenv
fi

# Check whether virtualenvwrapper module is installed
source `which virtualenvwrapper_lazy.sh` &>/dev/null
if [ $? -ne 0 ]; then
    echo "virtualenvwrapper not found. Installing virtualenvwrapper..."
    sudo apt-get install -y virtualenvwrapper
fi

# Ensure that virtualenvwrapper is loaded on shell startup
echo "source `which virtualenvwrapper_lazy.sh`" >> ~/.bashrc
# Apply the change immediately for this script
source ~/.bashrc

# Create a new virtual environment named greenwise
mkvirtualenv greenwise --python=$(which python3)

echo "You can now activate the greenwise environment using 'workon greenwise'. To deactivate, use 'deactivate'."
