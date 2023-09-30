Title: Raspberry Cat Feeder
Date: 2023-09-22 
Tags: raspberry pi, python, blender
Slug: raspberry-cat-feeder
Author: DGP
Summary: An automatic cat feeder powered by a raspberry pi

The Raspberry Cat Feeder is a an automatic cat feeder powered by [Raspberry Pi](https://www.raspberrypi.com/ "raspberrypi.com").  The [rcf] can be programmed to feed at prescribed intervals or on demand through a web interface.  

Design goals for the project include:
- assembled from inexpensive, commonly accessible hardware using simple hand tools available to the average DIYer.
- provide food for extended away intervals
- be reliable and low maintenance
- be rodent and vermin "*proof* "


## Mechanical
![Feeder](/images/cat_feeder_still.png)


A short animation showing the mechanical concept. [Cat Feeder](https://youtu.be/JP9D95I43UQ)


## Circuit Diagram

A circuit diagram is shown below as well as a list of the major components used in the prototype version built.  The selection of these components was strictly based on parts available on hand at the time.

![Circuit Diagram](/images/cat_feeder_circuit_diagram.png "Diagram")

N.B. some of these relay modules may behave differently. Caution should be exercised - transistor driver circuits and or pull up/down resistors may
be required to ensure reliable relay operation and or damage to the pi.

## Software 

The cat feeder code is largely written in Python and utilizes the [GPIOZero](https://gpiozero.readthedocs.io/en/stable/) library for driving board's input/output. 

here is an early version of the basic motor control:



```python
#! /usr/bin/python3

from time import sleep
from gpiozero import DigitalOutputDevice
from gpiozero import OutputDevice
from gpiozero import Button

import history

switch = Button(4)

relay = OutputDevice(3,active_high=True,initial_value=True,pin_factory=None)

def motor_off():
    # active low relay so reverse logic
    print("off")
    relay.on()
    history.write_event()

def motor_on():
    # active low relay so reverse logic
    print("on")
    relay.off()

def feed():
    print("feed")

    delay = 24.0
    dwell = 2
    motor_on()
    sleep(dwell) #move off limit switch
    made = switch.wait_for_press()
    print("switch")
    if made:
        motor_off()
```


The web interface uses the NiceGUI framework.  

---
[rcf]:

#raspberry-cat-feeder 