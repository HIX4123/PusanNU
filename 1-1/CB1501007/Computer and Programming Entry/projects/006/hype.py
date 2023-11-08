# -*- coding:utf-8 -*-

import string

def somunja(word):
    alpha = list(string.ascii_lowercase)
    flag = True
    for w in list(word):
        if w not in alpha:
            flag = False
    return flag

hype = open("hype.txt", "w")
Hype = """
Baby, got me looking so crazy
빠져버리는 daydream
Got me feeling you
너도 말해줄래

누가 내게 뭐라든
남들과는 달라 넌
Maybe you could be the one
"""

Lyrics = Hype.split()
for i, w in enumerate(Lyrics):
    if somunja(w) == True:
        hype.write(f"{w}\n")