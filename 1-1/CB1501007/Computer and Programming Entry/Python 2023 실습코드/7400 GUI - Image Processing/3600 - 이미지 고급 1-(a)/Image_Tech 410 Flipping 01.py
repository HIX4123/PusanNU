"""
Program name: image_flips_1.py
Objective: Rotate by multiples of 90 degreews and
flip vertically and horizontally.

Keywords: canvas, image, rotate, flip,  jpg, PIL, Python Imaging Library
============================================================================79

Explanation: The basic image re-orientation operations..

Author:          Mike Ohlson de Fine

"""
import tkinter
from PIL import Image, ImageTk        # 반드시 tkinter 다음에 선언에야 한다.
from PIL import ImageFont, ImageDraw

im_1 = Image.open("chapter_6/dusi_leo_1.jpg")
im_out_1 = im_1.transpose(Image.FLIP_LEFT_RIGHT)
im_out_2 = im_1.transpose(Image.FLIP_TOP_BOTTOM)
im_out_3 = im_1.transpose(Image.ROTATE_90)
im_out_4 = im_1.transpose(Image.ROTATE_180)
im_out_5 = im_1.transpose(Image.ROTATE_270)

#im_out_1.show()
#im_out_2.show()
im_out_3.show()
#im_out_4.show()
#im_out_5.show()

