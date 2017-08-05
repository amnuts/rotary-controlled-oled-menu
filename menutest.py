import sys
from time import sleep

from Menus.Menu import Menu
from Input.Rotary import Rotary

m = Menu([
    "First line",
    "A second menu option",
    "Now to the third",
    "On to the forth",
    "Follow the fifth",
    "Support the sixth"
])

r = Rotary(**{'menu': m, 'clk': 29, 'dt': 31, 'btn': 37})

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
