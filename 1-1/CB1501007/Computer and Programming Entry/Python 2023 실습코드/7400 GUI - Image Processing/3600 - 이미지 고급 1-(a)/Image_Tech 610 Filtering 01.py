"""
Program name: image_pileof_filters_1.py
Objective: Apply a bunch of filters to an image.

Keywords: Image, filters, png,
============================================================================79

Explanation:FILTERS
Creates a new image by applying predefined filters.

Author:          Mike Ohlson de Fine

"""
# image_pileof_filters_1.py
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import tkinter
from PIL import Image, ImageTk  # 반드시 tkinter 다음에 선언에야 한다.
from PIL import ImageFont, ImageDraw, ImageFilter

im_1 = Image.open("chapter_6/russian_doll.png")

im_2  = im_1.filter(ImageFilter.BLUR)
im_3  = im_1.filter(ImageFilter.CONTOUR)
im_4  = im_1.filter(ImageFilter.DETAIL)
im_5  = im_1.filter(ImageFilter.EDGE_ENHANCE)
im_6  = im_1.filter(ImageFilter.EDGE_ENHANCE_MORE)
im_7  = im_1.filter(ImageFilter.EMBOSS)
im_8  = im_1.filter(ImageFilter.FIND_EDGES)
im_9  = im_1.filter(ImageFilter.SMOOTH)
im_10 = im_1.filter(ImageFilter.SMOOTH_MORE)
im_11 = im_1.filter(ImageFilter.SHARPEN)

im_2.save("Enhance/russian_doll_BLUR.png")
im_3.save("Enhance/russian_doll_CONTOUR.png")
im_4.save("Enhance/russian_doll_DETAIL.png")
im_5.save("Enhance/russian_doll_EDGE_ENHANCE.png")
im_6.save("Enhance/russian_doll_EDGE_ENHANCE_MORE.png")
im_7.save("Enhance/russian_doll_EMBOSS.png")
im_8.save("Enhance/russian_doll_FIND_EDGES.png")
im_9.save("Enhance/russian_doll_SMOOTH.png")
im_10.save("Enhance/russian_doll_SMOOTH_MORE.png")
im_11.save("Enhance/russian_doll_SHARPEN.png")


