import sys
from time import sleep

from Oled.Menu import Menu, MenuAction, MenuParent
from Oled.Rotary import Rotary

m = Menu([
    MenuAction("First line", lambda: print("First line")),
    MenuAction("A second menu option", lambda: print("Second line")),
    MenuParent("Now to the third", [
        MenuAction("First sub-option", lambda: print("First sub-option")),
        MenuAction("Second sub-option", lambda: print("Second sub-option")),
        MenuParent("Third sub-option", [
            MenuAction("First sub-sub-option", lambda: print("First sub-sub-option")),
            MenuAction("Second sub-sub-option", lambda: print("Second sub-sub-option")),
            ]),
        ]),
    MenuAction("On to the forth", lambda: print("Fourth option")),
    MenuAction("Follow the fifth", lambda: print("Fifth option")),
    MenuAction("Support the sixth", lambda: print("Sixth option")),
])

try:
    r = Rotary(**{'menu': m, 'clk': 16, 'dt': 18, 'btn': 22})
    if len(sys.argv) > 1:
        if sys.argv[1] == 'clear':
            m.blank(True)
        else:
            m.set_highlight(int(sys.argv[1]))
            m.render()
    else:
        m.render()
    while True:
        sleep(1)
except KeyboardInterrupt:
    m.blank(True)
