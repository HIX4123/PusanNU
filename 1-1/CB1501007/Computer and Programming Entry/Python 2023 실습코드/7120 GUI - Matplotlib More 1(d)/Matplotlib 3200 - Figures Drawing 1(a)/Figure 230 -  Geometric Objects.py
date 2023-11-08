import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path


# circle
circle = patches.Circle((0,0),radius=1.,color = '.75')
plt.gca().add_patch(circle)

#rectangle
rect = patches.Rectangle((2.5, -.5), 2., 1., color = '.75')
plt.gca().add_patch(rect)

# Ellipse
ellipse = patches.Ellipse((0, -2.), 2., 1., angle = 45., color ='.75')
plt.gca().add_patch(ellipse)

# Path
verts = [
    (3., -2), # left, bottom
    (3., -1.), # left, top
    (4., -1.), # right, top
    (4., -2), # right, bottom
    (3., -2.), # ignored
    ]

codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

path = Path(verts, codes)

patch = patches.PathPatch(path, color='.75')  #  facecolor='orange', lw=2,
plt.gca().add_patch(patch)
plt.gca().set_xlim(-2,2)
plt.gca().set_ylim(-2,2)

plt.axis('scaled')
plt.grid(True)
plt.show()
