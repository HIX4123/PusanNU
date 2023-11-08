

Work={}

day1=(2023,  3,  4, 1500)
day2=(2023,  3,  5, 3450)
day3=(2023,  6, 14,  890)
day4=(2022, 12,  7, 5649)
day5=(2021,  7, 12, -892)

for tok in [day1, day2, day3, day4, day5] :
    date= tok[:3]
    Work[date] = tok[3]


for w in Work :
    print(f"key= {w},  value= {Work[w]}")