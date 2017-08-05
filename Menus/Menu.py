import os

from Adafruit import SSD1306
from RPi import GPIO
from PIL import Image, ImageDraw, ImageFont


class Menu:

    def __init__(self, options):
        self.options = options
        self.onOption = -1

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
        self.blank()
        self.build(highlight)
        self.oled.image(self.image)
        self.oled.display()

    def build(self, highlight=None):
        top = -1
        for x in range(len(self.options)):
            fill = 1
            if highlight == x:
                at_row_height = 12 * highlight
                self.draw.rectangle([0, at_row_height - 1, self.oled.width, at_row_height + 12], outline=0, fill=1)
                fill = 0
            self.draw.text((3, top + 2), self.options[x], font=self.font, fill=fill)
            top += 12
