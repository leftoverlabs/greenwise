#!/bin/bash

# define location where the virtual environment will be created
PROJECT_DIR=~/greenwise

# Check if the virtualenv module is installed
virtualenv --version &>/dev/null
if [ $? -ne 0 ]; then
    echo "virtualenv not found. Installing virtualenv..."
    sudo apt-get install -y python3-virtualenv
fi

# Check if the virtualenvwrapper module is installed
source /usr/share/virtualenvwrapper/virtualenvwrapper_lazy.sh &>/dev/null
if [ $? -ne 0 ]; then
    echo "virtualenvwrapper not found. Installing virtualenvwrapper..."
    sudo apt-get install -y virtualenvwrapper
fi

# Source the virtualenvwrapper_lazy.sh script
source /usr/share/virtualenvwrapper/virtualenvwrapper_lazy.sh

# Create a new virtual environment named greenwise
mkvirtualenv --python=$(which python3) greenwise -a $PROJECT_DIR

echo "You can now activate the greenwise environment (which is now associated with your project) using 'workon greenwise'. To deactivate, use 'deactivate'."
