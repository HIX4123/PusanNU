#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh'w Work
# Author:      Cho
# Created:     2020-06-18
#-------------------------------------------------------------------------------

number = 80
pi = 3.14
name = "pynative.com"
complexNum = 1+2j

sampleList  = ["Eric", "Scott", "Kelly"]
studentDict = {"John":80, "Eric":70, "Donald":90}
sampleTuple = ("Sam","Developer", 10000)
sampleSet   = {11, 22, 33, 44, 55}

flag = isinstance(number, int)
print(number,'is an instance of int?', flag)

flag = isinstance(pi, float)
print(pi,'is an instance of float?', flag)

flag = isinstance(complexNum, complex)
print(complexNum, "is an instance of a complex number?", flag)

flag = isinstance(name, str)
print(name,'is an instance of String?', flag, "\n")

flag = isinstance(sampleList, list)
print(sampleList,'is instance of list?', flag)

flag = isinstance(studentDict, dict)
print(studentDict,'is instance of Dictionary?', flag)

flag = isinstance(sampleTuple, tuple)
print(sampleList,'is instance of Tuple?', flag)

flag = isinstance(sampleSet, set)
print(studentDict,'is instance of Set?', flag)