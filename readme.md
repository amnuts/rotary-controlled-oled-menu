# Rotary encoder controlled menu on a 128x32 OLED display

Some code from playing around with getting a menu, or set of menus, to work by using a rotary encoder.

The output of this is very specifically for a 128x32 OLED display that uses the SSD1306 chip.

### External libraries
 
This uses the [Adafruit_SSD1306 library](https://github.com/adafruit/Adafruit_Python_SSD1306/) (or, at least, I took the files I wanted to use and modified them to only be specifically about a 128x32 display using IC2) as well as [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO) and [Pillow](https://pypi.python.org/pypi/Pillow) for drawing the display image.

### Hardware setup

The library is set up to use pins in the _board_ numbering scheme, not the _BCM_ numbering scheme, and was tested on a Raspberry Pi 3.

The pins used for the example are as follows:

*Power:*
* 4 - 5v
* 6 - GND

*OLED:*

* 3 - SDA
* 5 - SCL

*Rotary:*

* 16 - CLK
* 18 - DT
* 22 - SW


