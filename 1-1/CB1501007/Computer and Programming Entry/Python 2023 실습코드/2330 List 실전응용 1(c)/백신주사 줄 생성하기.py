#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-03-21
#-------------------------------------------------------------------------------
F="female"
M="male"

Q=[ (45,F,"KimS"),    (56,M,"Ted"),    (11,M,"potato"), (15,M,"현빈"),
    (67,F,"Claris"), (47,F,"Mary"), ( 34,F,"부산사람"), ( 78,F,"Kyiv"),
    ( 34,M,"Doris"), (41,M,"Denny"), ( 9,M,"꼬마야"), (75,M,"Cofiy"),
    (69,F,"Emery"),   (49,M,"Costico"), ( 67,M,"Oldheny"), (34,M,"팽수"),
    ( 5,F,"Cotton"),  (12,F,"Claudia"), (62,F,"종달새"), ( 13,M,"오달수"),
]

Old=[]
Child=[]
for w in Q:
    print(w)
    if w[0] >= 65 :
        Old.append(w)
    if 1 <= w[0] <=15 :
        Child.append(w)


