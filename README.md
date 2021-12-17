# About
Implemets a class used for autonomous configuration of VyOS router and check if Vyos is able to trade packets properly

# Usage
Run configure.py python program to send configurations to the Vyos device:

```sh
python3 configure.py
```


Run robot script to test wether the devices are trading packets normally:
```sh
robot VyosTest.rst
```

# Configuration
You have to set the appropriate ssh private key in sut.
Edit config.txt and device.txt in accordance to your devices and the configurations intended to be sent