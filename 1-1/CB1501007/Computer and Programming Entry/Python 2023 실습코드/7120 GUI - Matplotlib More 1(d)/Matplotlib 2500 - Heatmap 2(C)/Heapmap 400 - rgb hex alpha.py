#-------------------------------------------------------------------------------
# Name:        module1
# Author:      algor
#-------------------------------------------------------------------------------

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))

my = (230, 134, 45 )
r,g,b = my

Hex= rgb_to_hex( r, g, b )
RGB= hex_to_rgb( Hex )

print(f" RGB= {my}, Hex={Hex}")
print(f" Hex={Hex}, RGB={RGB}")

import matplotlib

print(matplotlib.colors.to_hex([ 0.47, 0.0, 1.0 ]))
print(matplotlib.colors.to_hex([ 0.7, 0.321, 0.3, 0.5 ], keep_alpha=True))

# True는 투명도 값을 사용한다는 의미
# keep_alpha, bool, default: False
# If False, use the #rrggbb format, otherwise use #rrggbbaa.

print( matplotlib.colors.to_rgb("#aabbcc")   )
print( matplotlib.colors.to_rgb("#ddee9f")   )
print( matplotlib.colors.to_rgb("#b2524c80") )
