#--------------------------------------------------------
# Author:      Zoh Que
# Created:     27-01-2023
#--------------------------------------------------------

w=list("34,567,76,87,78,56,445,667,90".split(","))
print(w)

w[0:5] = list(map(int, w[0:5]))
print(w)