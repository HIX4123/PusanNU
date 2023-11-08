
A = { 1, 2, 3, 4, 5 }  # { }는 집합을 표시한다. [ ] 는 리스트
B = { 4, 5, 6, 7, 8 }

# use - operator on A
# Output: {1, 2, 3}
print("Difference = ", (A - B))

print("Intersection = ", (A & B))

print("Symmetric Difference=", A ^ B) #XOR