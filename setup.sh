#!/bin/bash

#Install scripts in target directory
mkdir -p /home/pi/Control_GPIO_UDP
cp *.py /home/pi/Control_GPIO_UDP/.
cp config.cfg /home/pi/Control_GPIO_UDP/.

#Install service script in /etc/init.d
sudo chmod a+x service_manager
sudo cp service_manager /etc/init.d/.
sleep 1
sudo update-rc.d service_manager defaults
