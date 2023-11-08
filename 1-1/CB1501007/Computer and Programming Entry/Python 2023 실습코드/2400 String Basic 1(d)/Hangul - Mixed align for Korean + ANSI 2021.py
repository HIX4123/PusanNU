#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kate
#
# Created:     14-03-2021
# Copyright:   (c) Kate 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import unicodedata

def left_align(input_s="", max_size=40):
    l = 0
    for c in input_s:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l+=2
        else:
            l+=1
    return " "*(max_size-l)+input_s

def right_align(input_s="", max_size=40):
    l = 0
    for c in input_s:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l+=2
        else:
            l+=1
    return input_s+" "*(max_size-l)
a = "abc"
b = "이승훈"

print(left_align("abc", 12))
print(left_align("부산대학교", 12))
print(left_align("abc", 20))
print(left_align("부산대학교", 20))
print(left_align("abc", 22))
print(left_align("부산대학교", 22))