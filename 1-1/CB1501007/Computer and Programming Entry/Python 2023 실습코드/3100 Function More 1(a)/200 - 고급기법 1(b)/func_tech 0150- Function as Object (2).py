
G= 0

def BOY():
    global G
    G += 1
    print(G, "Boy Boy My Boy")



BOY()
BOY()

GIRL = BOY

GIRL()
GIRL()
GIRL()

del BOY
#BOY() # NameError: name 'BOY' is not defined
GIRL()

print(GIRL.__name__)