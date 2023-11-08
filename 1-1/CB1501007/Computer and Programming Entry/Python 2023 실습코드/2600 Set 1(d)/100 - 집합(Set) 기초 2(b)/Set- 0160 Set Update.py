

sa = {1,3}
print("STEP 1: ", sa)

#sa[0] ????

sa.add(2)
print("STEP 2: ",sa)


# add multiple elements
sa.update([2,3,4])
print("STEP 3: ",sa)

sa.update([20,30,40]) #리스트
print("STEP 4: ",sa)


# add list and set
sa.update([4,5], {100,6,8})
print("STEP 5: ",sa)

for w in sa :
    print(w)