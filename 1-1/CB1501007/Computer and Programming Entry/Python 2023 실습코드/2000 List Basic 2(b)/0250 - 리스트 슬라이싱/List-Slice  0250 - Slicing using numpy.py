import numpy as np


Callpos=[ [ 45,356], [ 455,  234], [190, 123], [  6, 765],
          [325, 36], [  53,  114], [219,  89], [327,  15],
          [105,426], [ 135,  84],  [402, 233], [ 57, 515],
          [145,656], [ 115, 235],  [  9, 270], [623,  76],
        ]


Xpos =  np.array(Callpos)[:, 0]  # 각 항목의 index-0 array
Ypos =  np.array(Callpos)[:, 1]  # 각 항목의 index-1 array
print(f" Xpos= {Xpos}")
print(f" Ypos= {Ypos}")

Xmax = max( Xpos )
Xmin = min( Xpos )
Ymax = max( Ypos )
Ymin = min( Ypos )

print(f" Xmax, Xmin, Ymax, Ymin = {Xmax, Xmin, Ymax, Ymin}")

Xdiff = Xmax - Xmin
Ydiff = Ymax - Ymin
Gkan = 12   # 그리드의 칸의 수 12 by 12
Xgap = Xdiff/Gkan
Ygap = Ydiff/Gkan

GridBox={}
for token in Callpos :
    xi = int( (token[0]- Xmin) / Xgap )
    yi = int( (token[1]- Ymin) / Ygap )
    print(f" token={token[0]:3}, {token[1]:3}, (xi,yi)={xi,yi}")
    GridBox[(xi,yi)].append(token)