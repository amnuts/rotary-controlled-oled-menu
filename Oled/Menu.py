import os
import threading

from PIL import Image, ImageDraw, ImageFont
from RPi import GPIO

from Oled import SSD1306


class Menu:

    def __init__(self, options=[]):
        self.options = options
        self.highlight_option = None
        self.row_count = 3

        self.oled = SSD1306.SSD1306_128_32(rst=None, gpio=GPIO)
        self.oled.begin()
        self.oled.clear()
        self.oled.display()

        self.image = Image.new('1', (self.oled.width, self.oled.height))
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.truetype(os.path.dirname(__file__) + '/pixel_arial_11.ttf', 8)

        self.render_thread = None

    def set_options(self, options):
        self.options = options
        self.highlight_option = None

    def set_highlight(self, highlight):
        if highlight is None:
            self.highlight_option = None
        elif highlight < 0:
            self.highlight_option = 0
        elif highlight >= len(self.options):
            self.highlight_option = len(self.options) - 1
        else:
            self.highlight_option = highlight

    def change_highlight(self, by):
        self.set_highlight(0 if self.highlight_option is None else self.highlight_option + by)

    def blank(self, draw=False):
        self.draw.rectangle((-1, -1, self.oled.width + 1, self.oled.height + 1), outline=0, fill=0)
        if draw:
            self.oled.image(self.image)
            self.oled.display()

    def render(self):
        if self.render_thread is None or not self.render_thread.is_alive():
            self.render_thread = threading.Thread(target=self.__render)
            self.render_thread.start()

    def __render(self):
        self.blank()
        self.__build()
        self.oled.image(self.image)
        self.oled.display()

    def __build(self):
        # adjust the start/end positions of the range
        if (self.highlight_option is None) or (self.highlight_option < self.row_count):
            start = 0
            end = self.row_count
        elif self.highlight_option >= (len(self.options) - self.row_count):
            end = len(self.options)
            start = end - self.row_count
        else:
            start = self.highlight_option
            end = start + self.row_count

        # draw the menu options
        top = 0
        for x in range(start, end):
            fill = 1
            if self.highlight_option is not None and self.highlight_option == x:
                self.draw.rectangle([0, top, self.oled.width, top + 11], outline=0, fill=1)
                fill = 0
            self.draw.text((3, top + 1), self.options[x], font=self.font, fill=fill)
            top += 10
