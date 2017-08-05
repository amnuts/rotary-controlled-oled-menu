import sys

from Menus.Menu import Menu

m = Menu([
    "First line",
    "A second menu option",
    "Now to the third",
    "On to the forth",
    "Follow the fifth",
    "Support the sixth"
])

if len(sys.argv) > 1:
    if sys.argv[1] == 'clear':
        m.blank(True)
    else:
        m.render(int(sys.argv[1]))
else:
    m.render()
