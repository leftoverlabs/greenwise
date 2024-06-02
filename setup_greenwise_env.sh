#!/bin/bash

# define location where the virtual environment will be created
PROJECT_DIR=~/greenwise

# Update package list
# sudo apt-get update

# Check if the virtualenv module is installed
virtualenv --version &>/dev/null
if [ $? -ne 0 ]; then
    echo "virtualenv not found. Installing virtualenv..."
    sudo apt-get install -y python3-virtualenv
fi

# Check if the virtualenvwrapper module is installed
source /usr/local/bin/virtualenvwrapper.sh &>/dev/null
if [ $? -ne 0 ]; then
    echo "virtualenvwrapper not found. Installing virtualenvwrapper..."
    sudo apt-get install -y virtualenvwrapper
fi

# set up virtualenvwrapper environment variables
export WORKON_HOME=~/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=$(which python3)

# Source the virtualenvwrapper.sh script
source /usr/local/bin/virtualenvwrapper.sh

# Create a new virtual environment named greenwise
mkvirtualenv greenwise -a $PROJECT_DIR

echo "You can now activate the greenwise environment using 'workon greenwise'. To deactivate, use 'deactivate'."
