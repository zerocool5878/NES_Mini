#Zerocool5878 non NFC Mini NES
We have been stuck editing STL files for a while. I have redrawn the case in solidworks 2013 to make editing easy. Keep in mind that my version is no NFC. If you would like NFC or Ethernet access you will have to draw that in. It also has a few other handy things built in.

##Features

- Both Daftmike original USB and Evan USB. Just unsuppress EvanUSB and you will be left with daftmike USB

- Integrated fan duct into the top lid. You will need to install 3mm nuts in the nut traps which is a bit challenging but I did it with a pair of tweezers. The fan folder can also be suppressed so you can print it without the duct. 

- The button/led holder is for 7mm switches and may need to be widened for your printer as the tolerance is tight.


##Prerequisites
- 3D printed case
- raspberry pi 3
- micro SD card installed retropie image (or another frontend over retropie)
- latching switch, momentary switch, No-NFC NES board, 30mm fan
- momentart switch should be connected to GPIO 24 and ground
 
##Installing scripts
- Use this line to install the python file, setup local network, and configure autostart at startup

```
wget https://raw.githubusercontent.com/zerocool5878/NES_Mini/master/setup.sh -v -O setup.sh; sudo chmod +x setup.sh; ./setup.sh; rm -rf setup.sh
```

##Note:
If anyone wants to draw in the NFC stuff or ethernet and put all the features used to do that in a folder like above I would be happy to push it to the github and give you the credit. 