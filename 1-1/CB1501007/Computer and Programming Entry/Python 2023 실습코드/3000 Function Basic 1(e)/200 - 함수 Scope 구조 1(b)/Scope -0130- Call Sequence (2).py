
def fa():
    print("In fa()")
    return

def fb():
    print("In fb()")
    return

def outer(x):
    if x < 0.5 :
        fa()
    else :
        fb()



fa( )
outer(1.1)