#!/bin/bash

# define location where the virtual environment will be created
PROJECT_DIR=~/greenwise

# Update package list
sudo apt-get update

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

# set up virtualenvwrapper environment variables
export WORKON_HOME=~/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=$(which python3)

# Source the virtualenvwrapper script
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh  # adjusted path

# Create a new virtual environment named greenwise
mkvirtualenv greenwise -a $PROJECT_DIR

echo "You can now activate the greenwise environment using 'workon greenwise'. To deactivate, use 'deactivate'."
