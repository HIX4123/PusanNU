
def switch1(x):
    return {
        '1': "하나요",
        '2': "둘이요",
        '3': "셋이요",
        '4': "넷이요",
    }.get(x, "이것 뭐요 ?") #default

t1 = switch1('1')
t2 = switch1('4')
t3 = switch1('9')


print(t1, t2, t3)


