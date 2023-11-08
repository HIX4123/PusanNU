#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------


import re

print("-------- group -------")
phonebook="Customer number: 232454, Date: February 12, 2011"

print("\n 첫번째 찾아진 원소의 정보 출력하기 ")
mo = re.search("\d+",phonebook )
print("group()=",    mo.group())
print("span() =",    mo.span())
print("start() =",   mo.start()) # span()[0]
print("end() = ",    mo.end())
print("span()[0]=",  mo.span()[0])
print("span()[1]=",  mo.span()[1])  #\.   .meta-문자

print("\n 매치된 원소의 일부를 출력하기 ")
mo2 = re.search("([0-9]+).*: (.*)", phonebook)
print("group( ) =",    mo2.group())   # 전체
print("group(1) =",    mo2.group(1))  # 첫번째 괄호
print("group(2) =",    mo2.group(2))
print("group(1,2) =",  mo2.group(1,2))


print("\n 매치된 원소의 일부를 출력하기2 ")
mytext=" This is:67 year Boy Crazy \
 John:45 is old good boy Mary:34 후후 Bradford:78 old boy"
mo2 = re.finditer("([A-Z]\w+):(\d+)", mytext)
for no, mym in enumerate(mo2) :
    print ("(%4d 부터 %4d)까지 " % mym.span() , end=" " )
    print (" => %8s" % mym.group() )
    print (" => %8s" % mym.group(1) )
    print (" => %8s" % mym.group(2) )







