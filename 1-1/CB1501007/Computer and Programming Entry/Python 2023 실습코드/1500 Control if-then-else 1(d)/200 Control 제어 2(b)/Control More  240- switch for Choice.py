switch = {
        "apple": "사과",
        "banana": "빠나나",
        "puppy": "강아지",
        "piggy": "똥돼지",
        "beer":  "맥주", }

t3 = switch.get( "figgy", "메롱메롱")
t1 = switch.get( "piggy", "메롱")
t2 = switch.get( "None",  "메롱")

print(t1, t2, t3)


