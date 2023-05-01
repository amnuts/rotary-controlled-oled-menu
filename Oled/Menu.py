import os
import threading
from dataclasses import dataclass, field
from typing import Union
from copy import deepcopy

from PIL import Image, ImageDraw, ImageFont
from RPi import GPIO

from Oled import SSD1306


@dataclass
class MenuAction:
    text: str
    action: callable = None


@dataclass
class MenuParent:
    text: str
    actions: list[MenuAction] = field(default_factory=list)


class Menu:
    def __init__(self, options: list[Union[MenuParent, MenuAction]] = None):
        if options is None:
            options = []
        self.options = options
        self.highlight_option = None
        self.current_menu_level = [(None, self.options)]
        self.row_count = 3

        self.oled = SSD1306.SSD1306_128_32(rst=None, gpio=GPIO)
        self.oled.begin()
        self.oled.clear()
        self.oled.display()

        self.image = Image.new('1', (self.oled.width, self.oled.height))
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.truetype(os.path.dirname(__file__) + '/pixel_arial_11.ttf', 8)

        self.render_thread = None

    def blank(self, draw=False):
        self.draw.rectangle((-1, -1, self.oled.width + 1, self.oled.height + 1), outline=0, fill=0)
        if draw:
            self.oled.image(self.image)
            self.oled.display()

    def change_highlight(self, by):
        self.set_highlight(0 if self.highlight_option is None else self.highlight_option + by)

    def set_highlight(self, highlight):
        options = self.__current_options()
        if highlight is None:
            self.highlight_option = None
        elif highlight < 0:
            self.highlight_option = 0
        elif highlight >= len(options):
            self.highlight_option = len(options) - 1
        else:
            self.highlight_option = highlight

    def render(self):
        if self.render_thread is None or not self.render_thread.is_alive():
            self.render_thread = threading.Thread(target=self.__render)
            self.render_thread.start()

    def perform_current_action(self):
        if self.highlight_option is None:
            return
        options = self.__current_options()
        if type(options[self.highlight_option]) is not MenuParent:
            options[self.highlight_option].action()
            return
        self.current_menu_level.append((self.highlight_option, options[self.highlight_option].actions))
        self.highlight_option = 0
        self.render()
        return

    def __render(self):
        self.blank()
        self.__build()
        self.oled.image(self.image)
        self.oled.display()

    def __build(self):
        options = self.__current_options()

        # adjust the start/end positions of the range
        if (self.highlight_option is None) or (self.highlight_option < self.row_count):
            start = 0
            end = self.row_count
        elif self.highlight_option >= (len(options) - self.row_count):
            end = len(options)
            start = end - self.row_count
        else:
            start = self.highlight_option
            end = start + self.row_count

        if start < 0:
            start = 0
        if end > len(options):
            end = len(options)

        # draw the menu options
        top = 0
        for x in range(start, end):
            fill = 1
            if self.highlight_option is not None and self.highlight_option == x:
                self.draw.rectangle([0, top, self.oled.width, top + 11], outline=0, fill=1)
                fill = 0

            if type(options[x]) is MenuParent:
                display_text = f"{options[x].text} {'>'*20}"
            else:
                display_text = options[x].text

            self.draw.text((3, top + 1), display_text, font=self.font, fill=fill)
            top += 10

    def __back(self):
        if len(self.current_menu_level) > 1:
            self.highlight_option, _ = self.current_menu_level.pop()
        self.render()

    def __current_options(self):
        _, orig_options = self.current_menu_level[-1]
        options = deepcopy(orig_options)
        if type(options) is MenuParent:
            options = options.actions
        if len(self.current_menu_level) > 1:
            options.insert(0, MenuAction(f"Back {'<'*20}", lambda: self.__back()))
        return options
