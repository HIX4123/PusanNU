
mylist = ["Gum", "wine", "Banana", "Gum", "Apple", "Beer", "Beer", "Soju", "Wine", "Beer"]
yourlist = ["Bread", "Udong", "Sake", "Banana", "Beer",  "Soju", "Wine", "Beer"]
myset  = set( mylist )
yourset = set (yourlist)


print("mylist = ", mylist)
print("Set으로 바뀐 이후", myset)


print("실험 3:", type( mylist), "size= ", len(mylist))
print("실험 4:", type( myset ), "size= ", len(myset ))


myset.pop()
print("실험 5:", myset, "size= ", len(myset ))

common =  (myset & yourset)
print("두 집합의 공통 intersection:", common)

common =  (myset | yourset)
print("두 집합의 합집합 union:", common)