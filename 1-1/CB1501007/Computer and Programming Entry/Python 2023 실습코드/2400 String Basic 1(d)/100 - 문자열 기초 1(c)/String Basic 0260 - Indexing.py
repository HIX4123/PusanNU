# str.index(sub[, start[, end]] )

# 단 없는 경우에는 오류가 난다. find( )와 다른 점


sentence = 'Pythoning programm is fun going home taking him.'

result = sentence.index('is fun')
print("Substring 'is fun':", result)


# Substring is searched in 'gramming is fun.'
print("> Out1 ", sentence.index('ing'))
print("> Out2 ", sentence.index('ing', 10))

# Substring is searched in 'gramming is '
print(sentence.index('g is', 10, -4))

# Substring is searched in 'programming'
# print(sentence.index('fun', 7, 18))

# result = sentence.index('Java')
# print("Substring 'Java':", result)