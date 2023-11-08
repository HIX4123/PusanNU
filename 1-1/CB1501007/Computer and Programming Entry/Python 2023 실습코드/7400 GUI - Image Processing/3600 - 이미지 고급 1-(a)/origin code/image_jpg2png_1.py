"""
Program name: image_jpg2png_1.py
Objective: Open a jpg format image file, display it and then save it as .png format.

Keywords: image format convert, jpg, png, PIL, Python Imaging Library
============================================================================79

Explanation: Open and save.
Of interest - the jpg file is 1.8 Megabyte and the resulting png is more than
twice as large at 4.6 Megabyte.

Author:          Mike Ohlson de Fine

"""
# images_jpg2png_1.py
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import Image
im_1 = Image.open("chapter_6/dusi_leo_1.jpg")
im_1.show()
im_1.save('chapter_6/dusi_leo_2.png', 'PNG')



