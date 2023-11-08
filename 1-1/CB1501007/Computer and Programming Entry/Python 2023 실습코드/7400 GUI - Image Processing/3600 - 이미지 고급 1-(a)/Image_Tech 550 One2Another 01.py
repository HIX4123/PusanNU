"""
Program name: images_one2another_1.py
Objective:Open one jpg and convert it to gif, png, bmp, tif formats.
Then take each of these resultant files and convert each in turn
to each of the others. This way we discover that the gif to jpg conversion
does not work. However gif DOES convert to png, tiff and bmp.
So the conversion route gif->png->jpg will work.

Keywords: image convert, jpg, gif, bmp, png, PIL, Python Imaging Library
============================================================================79

Explanation: This is an image format convversion test.
It attempts the conversion of each of the major formats into each of the
others. This way we discover that the gif to jpg conversion does not work.
However gif DOES convert to png, tiff and bmp.
So the conversion route gif->png->jpg will work.
"""

import tkinter
from PIL import Image, ImageTk        # 반드시 tkinter 다음에 선언에야 한다.
from PIL import ImageFont, ImageDraw

# Convert a jpg image to OTHER formats
im_1 = Image.open("chapter_6/test_pattern_1.jpg")
im_1.save('Trnas/Another_2.png', 'PNG')
im_1.save('Trnas/Another_3.gif', 'GIF')
im_1.save('Trnas/Another_4.tif', 'TIFF')
im_1.save('Trnas/Another_5.bmp', 'BMP')

# Convert a png image to OTHER formats
im_2 = Image.open("Trnas/Another_2.png")
im_2.save('Trnas/pattern_6.jpg', 'JPEG')
im_2.save('Trnas/pattern_7.gif', 'GIF')
im_2.save('Trnas/pattern_8.tif', 'TIFF')
im_2.save('Trnas/pattern_9.bmp', 'BMP')

# Convert a gif image to to OTHER formats
# It seems that gif->jph does not work
im_3 = Image.open("Trnas/Another_3.gif")
#im_3.save('/constr/pics1/test_pattern_10.jpg', 'JPEG')
# "IOError "cannot write mode P as JPEG"
im_3.save('Trnas/Rttern_11.png', 'PNG')
im_3.save('Trnas/Rttern_12.tif', 'TIFF')
im_3.save('Trnas/Rttern_13.bmp', 'BMP')

# Convert a gif image to to OTHER formats
im_4 = Image.open("Trnas/pattern_8.tif")
im_4.save('Trnas/Qttern_14.png', 'PNG')
im_4.save('Trnas/Qttern_15.gif', 'GIF')
im_4.save('Trnas/Qttern_16.tif', 'TIFF')
im_4.save('Trnas/Qttern_17.bmp', 'BMP')

# Convert a gif image to to OTHER formats
im_5 = Image.open("Trnas/pattern_9.bmp")
im_5.save('Trnas/Wttern_18.png', 'PNG')
im_5.save('Trnas/Wttern_19.gif', 'GIF')
im_5.save('Trnas/Wttern_20.tif', 'TIFF')
im_5.save('Trnas/Wttern_21.jpg', 'JPEG')
