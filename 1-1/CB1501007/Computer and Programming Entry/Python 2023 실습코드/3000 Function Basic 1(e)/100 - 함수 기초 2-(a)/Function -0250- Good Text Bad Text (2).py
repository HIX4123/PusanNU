
bad =["개", "똥", "띵", "막", "뽕"]


def is_good( T ):
    cnt = 0
    for w in bad :
        if w in T :
            cnt += 1
    if cnt == 0 : return( "CLEAN")
    if cnt <= 1 : return ("GOOD")
    if cnt <= 3 : return ("BAD")
    if cnt >= 4 : return ("FORBIDDEN")
# ----- end of is_good( ) ----------


##def is_clean( T ):
##    cnt = 0
##    for w in bad :
##        if w in T :
##           return ("BAD")
##
##    return("GOOD")

text  = "이것은 개바보같은 띵작이다 뽕? ."
text2 = " 개바보같은 똥똥똥똥 막띵작이다 홍홍홍."

print("[", text, " ] 문장은 ==>", is_good( text ))
print("[", text2, " ] 문장은 ==>", is_good( text2 ))

text = "엄마야 누나야 강변 살자"
print("[", text, " ] 문장은 ==>", is_good( text ))