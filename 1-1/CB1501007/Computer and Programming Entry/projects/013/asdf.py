import datetime

date = datetime.datetime.now()
# print("쌩(raw) date 문자열 = ", date)

# mys = f"{date:%y에서 %m월이고 날짜는 %d일} is on a {date:%A}"

# print(f"시간은 {date:%H}")
# print(f"분은 {date:%M}")
# print(f"초(second)는 {date:%S}")

N = 10000
for i in range(N):
    for j in range(N):
        s = i + j

print("operation time:", datetime.datetime.now() - date)
