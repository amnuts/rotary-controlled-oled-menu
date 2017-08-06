# Rotary encoder controlled menu on a 128x32 OLED display

Some code from playing around with getting a menu, or set of menus, to work by using a rotary encoder.

The output of this is very specifically for a 128x32 OLED display that uses the SSD1306 chip.

### External libraries
 
This uses the [Adafruit_SSD1306 library](https://github.com/adafruit/Adafruit_Python_SSD1306/) (or, at least, I took the files I wanted to use and modified them to only be specifically about a 128x32 display using IC2) as well as [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO) and [PIL](http://www.pythonware.com/products/pil/) for drawing the display image.




