import sys
from time import sleep

from Oled.Menu import Menu
from Oled.Rotary import Rotary

m = Menu([
    "First line",
    "A second menu option",
    "Now to the third",
    "On to the forth",
    "Follow the fifth",
    "Support the sixth"
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
