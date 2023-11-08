myin = input("Type an INT:")

print(f"myin = {myin}, type = {type(myin)}, binary = {bin(int(myin))}")

myin = list(bin(int(myin)))[2:]

for i in myin:
    if i == '1':
        print("1!")

print(myin.count('1'))