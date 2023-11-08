"""
Program name: image_blend_2.py
Objective: Blend two images together.

Keywords: Image, blend, png,
============================================================================79

Explanation: BLEND-> Image.blend(image1, image2, alpha) => image

Creates a new image by interpolating between the two given images,
using a multiplying constant alpha.
Both images must have the same size and mode.

The algebra:   out = image1 * (1.0 - alpha) + image2 * alpha

If alpha is 0.0, a copy of the first image is returned.
If alpha is 1.0, a copy of the second image is returned.
There are no restrictions on the alpha value.
If necessary, the result is clipped to fit into the allowed output range.

Author:          Mike Ohlson de Fine

"""
# image_blend_2.py
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from PIL import Image
im_1 = Image.open("chapter_6/100_canary.png")   #  mode is RGBA
im_2 = Image.open("chapter_6/100_cockcrow.png") #  mode is RGB
im_2 = im_2.convert("RGBA")       # Make both modes the same

# Various degrees of alpha
im_3 = Image.blend(im_1, im_2, 0.05) # 95% im_1, 5% im_2
im_4 = Image.blend(im_1, im_2, 0.2)
im_5 = Image.blend(im_1, im_2, 0.5)
im_6 = Image.blend(im_1, im_2, 0.6)
im_7 = Image.blend(im_1, im_2, 0.8)
im_8 = Image.blend(im_1, im_2, 0.95) # 5% im_1, 95% im_2


#im_3.show()
im_3.save("fiery_lion_1.png")
im_4.save("fiery_lion_2.png")
im_5.save("fiery_lion_3.png")
im_6.save("fiery_lion_4.png")
im_7.save("fiery_lion_5.png")
im_8.save("fiery_lion_6.png")

