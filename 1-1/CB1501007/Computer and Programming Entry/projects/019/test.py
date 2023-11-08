# Path: CB1501007\Computer and Programming Entry\projects\019\test.py


import re


code = """
book = 67 + lost
book = lost = (56 + 89) / goof
56 = goof - 90 * yoo
goo - 90
best = ioo god + 900 + 1
good[4] = good[-1] + 1 + 100
"""


my = r"[a-zA-Z]+[ ]+=[ ]+\w+"
out = re.findall(my, code)
for w in out:
    print(w)
