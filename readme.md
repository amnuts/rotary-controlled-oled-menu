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

### Usage

The menu is set up as a combination of `MenuAction` items and `MenuParent` items, which can contain other `MenuParent` and `MenuAction` items.

For example, you might define your menu system such as:

```python
menu = Menu([
    MenuAction("First line", lambda: print("First line")),
    MenuAction("A second menu option", lambda: print("Second line")),
    MenuParent("Now to the third", [
        MenuAction("First sub-option", lambda: print("First sub-option")),
        MenuAction("Second sub-option", lambda: print("Second sub-option")),
        MenuParent("Third sub-option", [
            MenuAction("First sub-sub-option", lambda: print("First sub-sub-option")),
            MenuAction("Second sub-sub-option", lambda: print("Second sub-sub-option")),
        ]),
        MenuAction("Fourth sub-option", lambda: print("Fourth sub-option")),
    ]),
    MenuAction("On to the forth", lambda: print("Fourth option")),
    MenuAction("Follow the fifth", lambda: print("Fifth option")),
    MenuAction("Support the sixth", lambda: print("Sixth option")),
])
```

The `MenuAction` objects all have a lambda which fires off when pushing the button on the rotary controller.

You don't have to use a lambda; you could use a function defined elsewhere, or a class method, or whatever you want - so long as it's callable.

To then start displaying the menu and interacting with it, you need to create a new instance of the `Rotary` class, passing in the menu you want to use as well as defining the pins that the rotary controller uses, and then render.

For example:

```python
Rotary(**{"menu": menu, "clk": 16, "dt": 18, "btn": 22})
menu.render()
```
