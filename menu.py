import RPi.GPIO
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from Adafruit import SSD1306

menu = [
    "First line",
    "A second menu option",
    "Now to the third",
    "On to the forth",
    "Follow the fifth",
    "Support the sixth"
]

fontSize = 8
rowPadding = 1
rowMargin = 1
rowHeight = fontSize + (rowPadding * 2)

oled = SSD1306.SSD1306_128_32(rst=None, gpio=RPi.GPIO)
oled.begin()
oled.clear()
oled.display()

image = Image.new('1', (oled.width, oled.height))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('pixel_arial_11.ttf', fontSize)

# and draw a black filled box to clear the image. (usually in loop)
draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

at = 1
top = -1
for x in range(len(menu)):
    fill = 1
    if at == x:
        atRowHeight = rowHeight * at
        print '{}/{} = {}, {}, {}, {}'.format(x, at, 0, atRowHeight, oled.width, atRowHeight + atRowHeight)
        draw.rectangle([0, atRowHeight - rowPadding, oled.width, atRowHeight + rowHeight], outline=0, fill=1)
        fill = 0
    draw.text((3, top + rowPadding), menu[x], font=font, fill=fill)
    top += rowHeight

oled.image(image)
oled.display()
