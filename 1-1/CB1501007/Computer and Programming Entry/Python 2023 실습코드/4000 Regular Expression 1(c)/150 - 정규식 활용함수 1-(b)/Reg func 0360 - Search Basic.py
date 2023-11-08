#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-27
#-------------------------------------------------------------------------------


#!/usr/bin/python3
import re

line = "Cats are smarter than dogs crazy Bus are fast"
# 사람은 are 동물이다.  No Good are Books"

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print ("group() : ", searchObj.group())
   print ("group(1) : ", searchObj.group(1))
   print ("group(2) : ", searchObj.group(2))
else:
   print ("Nothing found!!")

print("\n Another Search\n")
searchObj = re.search( r'((.*?) are (.*?) .*)', line, re.M|re.I)

if searchObj:
   print ("group() : ", searchObj.group())
   print ("group(1) : ", searchObj.group(1))
   print ("group(2) : ", searchObj.group(2))
else:
   print ("Nothing found!!")