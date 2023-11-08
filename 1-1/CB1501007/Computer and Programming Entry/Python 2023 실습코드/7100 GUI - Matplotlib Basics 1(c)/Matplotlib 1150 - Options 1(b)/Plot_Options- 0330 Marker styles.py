##character           description
##================    ===============================
##   -                solid line style
##   --               dashed line style
##   -.               dash-dot line style
##   :                dotted line style
##   .                point marker
##   ,                pixel marker
##   o                circle marker
##   v                triangle_down marker
##   ^                triangle_up marker
##   <                triangle_left marker
##   >                triangle_right marker
##   1                tri_down marker
##   2                tri_up marker
##   3                tri_left marker
##   4                tri_right marker
##   s                square marker
##   p                pentagon marker
##   *                star marker
##   h                hexagon1 marker
##   H                hexagon2 marker
##   +                plus marker
##   x                x marker
##   D                diamond marker
##   d                thin_diamond marker
##   |                vline marker
##   _                hline marker


import matplotlib.pyplot as plt

mycolor = 'cornflowerblue'
plt.plot([1, 2, 3, 8], [1, 4, 9, 16],  marker='|', linestyle="-.",  color=mycolor, linewidth=3)
plt.plot([1, 2, 5, 7], [7, 11, 3, 5] ,  marker='s', linestyle="--",  color="red")
plt.plot([2, 3, 6, 9], [3, 6, 12, 10] ,  marker='h', linestyle="-",  color="black", linewidth=2)

plt.ylabel('some numbers')
plt.show()