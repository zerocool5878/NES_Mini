#!/bin/bash
# zerocool5878 NES script

sudo sed -i -e 's/# network_cmd_enable = false/network_cmd_enable = true/g' /opt/retropie/configs/all/retroarch.cfg
sudo sed -i -e 's/# network_cmd_port = 55355/network_cmd_port = 55355/g' /opt/retropie/configs/all/retroarch.cfg


cd ~
wget https://raw.githubusercontent.com/zerocool5878/NES_Mini/master/PiOnOffFanV5.py

cd /etc/
sudo chmod +x /etc/rc.local
sudo sed -i '15ipython /home/pi/PiOnOffFanV5.py &' rc.local

sudo reboot










