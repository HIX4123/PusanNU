

def yell(text):
    mys = text.upper()+ " !"
    return mys


# 함수는 first class, 변수로도 활용가능하다.

print( yell( "pusan viva" ))

bark = yell
print( bark( "nagari good" ))

del yell
#print( yell( "pusan viva" ))  Error
print( bark( "Sometimes" ))

print("bark.__name__= ", bark.__name__)