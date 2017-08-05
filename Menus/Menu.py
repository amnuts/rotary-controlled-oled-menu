import os

from Adafruit import SSD1306
from RPi import GPIO
from PIL import Image, ImageDraw, ImageFont


class Menu:

    def __init__(self, options):
        self.options = options
        self.onOption = None

        self.oled = SSD1306.SSD1306_128_32(rst=None, gpio=GPIO)
        self.oled.begin()
        self.oled.clear()
        self.oled.display()

        self.image = Image.new('1', (self.oled.width, self.oled.height))
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.truetype(os.path.dirname(__file__) + '/pixel_arial_11.ttf', 8)

    def blank(self):
        self.draw.rectangle((0, 0, self.oled.width, self.oled.height), outline=0, fill=0)

    def render(self, highlight=None):
        if highlight < 0:
            self.onOption = len(self.options) - 1
        elif highlight > len(self.options) - 1:
            self.onOption = 0
        else:
            self.onOption = highlight
        self.blank()
        self.build()
        self.oled.image(self.image)
        self.oled.display()

    def build(self):
        start = 0
        if self.onOption > 2:
            start = self.onOption - 2
        top = -1
        for x in range(start, start + 3):
            fill = 1
            if self.onOption == x:
                at_row_height = 12 * (self.onOption % 3)
                self.draw.rectangle([0, at_row_height - 1, self.oled.width, at_row_height + 12], outline=0, fill=1)
                fill = 0
            self.draw.text((3, top + 2), self.options[x], font=self.font, fill=fill)
            top += 12
