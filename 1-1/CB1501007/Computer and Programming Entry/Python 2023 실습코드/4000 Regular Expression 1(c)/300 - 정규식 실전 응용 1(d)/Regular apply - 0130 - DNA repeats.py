
import re


text = "cttggatagggatatataaagagtggggtggtggtaatagatataggtggtagggaaata"

print ( "입력 텍스트의 길이=", len( text) )

mypat = "(at|ag){2,}"  # at나 ag가 2회 이상 반복되는 것을 찾는다.

itlist = re.finditer( mypat, text )

print("{at ag}가 2회 이상 반복되는 것을 찾는다.")
for no, mym in enumerate(itlist) :
    print ("(%4d 부터 %4d)까지 " % mym.span() , end=" " )
    print (" => %8s" % mym.group() )


print("\n at ag만으로 2회 이상 반복되는 것을 찾는다.")

mypat = "(at){2,}|(ag){2,}"  # at ag만으로 2회 이상 반복되는 것을 찾는다.

itlist = re.finditer( mypat, text )

for no, mym in enumerate(itlist) :
    print ("(%4d 부터 %4d)까지 " % mym.span() , end=" " )
    print (" => %8s" % mym.group() )


