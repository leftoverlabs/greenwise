#!/bin/bash

# Set your WLAN country
read -p 'Enter WLAN country - e.g. CY for Cyprus' wlan_country
sudo raspi-config nonint do_wifi_country $wlan_country

# Check Wi-Fi is enabled
wifi_status=$(nmcli radio wifi)

if [[ $wifi_status == "disabled" ]]
then
  echo "Enabling WiFi"
  nmcli radio wifi on
fi

# List available networks
echo "Available Networks:"
nmcli dev wifi list

# Connect to a network
read -p 'Enter the SSID of the network you want to connect to: ' ssid
sudo nmcli --ask dev wifi connect $ssid
