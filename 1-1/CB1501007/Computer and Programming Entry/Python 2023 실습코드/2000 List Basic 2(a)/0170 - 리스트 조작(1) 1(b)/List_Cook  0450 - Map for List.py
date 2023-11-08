

#
slist = ["100", "26", "300", "-9", "700", "-123"]
ilist = [int(i) for i in slist ]
print("ilist= ", ilist)



jlist = list(map (int, slist)) # 또 다르게 바꾸는 방법
print("jlist= ", jlist)


slist = ["100.34", "0.26", "13.300", "-9.009", "-12.3"]
flist = [ float(i) for i in slist ]
print("flist= ", flist)