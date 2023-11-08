#copilot 허용 검토
#10에서 20까지 팩토리얼

import sys

input_s = sys.stdin.readline

mystring = input("Type a pharase:")
mylist = list(mystring.split())

print(f"mystring = {mystring}")
print(f"mylist = {mylist}")
myleng = len(mylist)

if myleng == 1: #첫자와 끝자
    print("크기는 1")
if myleng == 2:
    print("크기는 2")
if myleng == 3:
    print("크기는 3")
else:
    print("크기는 4 이상")