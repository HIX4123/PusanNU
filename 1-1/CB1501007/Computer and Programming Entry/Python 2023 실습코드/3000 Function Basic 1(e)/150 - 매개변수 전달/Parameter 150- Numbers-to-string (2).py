
def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
        3: "셋",
        4: "넷",
    }
    return switcher.get(argument, "nothing")

print(numbers_to_strings(4))
print(numbers_to_strings(7))

# 아 이것은....