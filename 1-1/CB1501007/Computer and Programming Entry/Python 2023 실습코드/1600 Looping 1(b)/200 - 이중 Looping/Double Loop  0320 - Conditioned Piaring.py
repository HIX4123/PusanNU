
people = ["P", "Q", "M", "Z"]

result = [ (p1, p2) for p1 in people for p2 in people]
print("Possible pair 1=", result )

result = [ (p1, p2) for p1 in people for p2 in people if p1 != p2]
print("\n\n All Ordered Pair 2=", result )

result = [(people[p1], people[p2]) for p1 in range(len(people)) \
                                      for p2 in range(p1+1,len(people))]

print("\n\n Unique Unordered pair 2=", result )

