
def addone(x):
    return x+1

def sqrone(x):
    return(x*x+1)

def cubeone(x):
    return(x*x*x+1)

print("funtion type=", type( addone))

funname= [ addone, sqrone, cubeone]

#함수를 내가 골라서...
for w in funname :  # 이것은 C/C++에 없는 기능
    val = w(7)
    print(val)


# List Comprehension를 이용하여 새로운 L
la = list( map( funname[1], list(range(11))))
