"""
Program name: image_offset_1.py
Objective: Make a reduced copy of an image.

Keywords: Image, offset, jpg,
============================================================================79

Explanation: Simple syntax to change image size

Author:          Mike Ohlson de Fine

"""

import tkinter
from PIL import Image, ImageTk        # 반드시 tkinter 다음에 선언에야 한다.
from PIL import ImageFont, ImageDraw, ImageChops

im_1 = Image.open("chapter_6/canary_a.jpg")

# adjust width and height to desired size
dx = 200
dy = 300

im_2 = ImageChops.offset(im_1, dx, dy)
im_2.show( )
im_2.save("Offset_2.jpg")

