

s = "e:\\Beginner"
s1 = "e:" "\\" "Beginner"
s2 = s1 + \
    "\\tst.py"

print(" s - This is a DOS path:", s)
print("s1 - This is a DOS path:", s1)
print("s2 - This is a DOS path:", s2)

s3 = "I contain 'single' quotes"

print(s3)

s6 = "s6 = I contain\t\t\tthree\t\t\ttabs"
s7 = "s7 = I contain a\t\v\tvertical tab"
s8 = "s8 = I contain a\t\a\tBELL, which you can hear"

print(s6)
print(s7)
print(s8)

s9  = "s9 = I contain a BACK\bSPACE"
s10 = "s10 = I contain a BACKK\bSPACE AND a \nNEWLINE and a \rLINEFEED"
s11 = "s11 = I ve got a FORM\fFEED!"

print(s9)
print(s10)
print()
print(s11)

s12 = "s12 = If Python doesn't know what the escape code\n" \
"means, it performs the identity operation!  \identity!"
s13 = "s13 = But if you don't know what a code means, don't use it!"

print(s12)
print(s13)
