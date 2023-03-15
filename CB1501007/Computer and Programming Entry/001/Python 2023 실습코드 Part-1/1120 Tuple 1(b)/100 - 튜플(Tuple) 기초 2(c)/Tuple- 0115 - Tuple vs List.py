

food = ("chicken", "pizza", "burger")
print(food)

drinks = "coke", "soda", "water"
print(drinks)

print()
#반복, 연결
print(food * 2)
print(food + drinks)
print(food[0], drinks [1])
print(food[1:3])

#값을 바꿀수 없음
#food[0] = "jockbal"

#튜플을 튜플로
menu = food , drinks
print(menu)

#Unpacking  풀어내는 과정을 언패킹
a, b, c = food
print(a, b, c)
print()

#튜플 -> 리스트, 아주 아주 중요
num_tuple = 1, 2, 3, 4, 5
num_list = list(num_tuple)
print(num_list)

#리스트 -> 튜플
num_tuple = tuple(num_list)
print(num_tuple)
print()


#인자값 전달
def multisum (*args) :
    res = 0;
    for i in args :
        res += i
    return res;

x = 17
y = 9
z = 5

print(multisum(x,y,z))
print(multisum(1,2,3,4,5,6,7,8,9,10))
print(multisum(1,3,5,7,9,11))