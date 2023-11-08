bad = ["똥", "개", "메롱", "바보", "쩐", "헐", "빡", "공부"]
count = 1
while True:
    point = 0
    msg = input("Type a message:")
    for i in bad:
        point -= msg.count(i)
        msg = msg.replace(i, "*")
    print(f"i = {count}, msg = {msg}, point = {point}")
    if point == 0:
        print("good!")
    elif point <= -10:
        print("bad!")
    if msg == "끝":
        break
    count += 1
