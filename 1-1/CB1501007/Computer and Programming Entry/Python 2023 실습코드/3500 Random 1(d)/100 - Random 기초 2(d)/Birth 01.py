#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-15
#-------------------------------------------------------------------------------

import random

random.seed(9871)

def birth():
    rval = random.random() # [0,1]
    if rval <= 0.5122 : return ("M")
    else : return( "F" )



def manseek( ) :
    bseq=""
    while(1) :
        sex = birth()
        if sex == 'M' :
            bseq += sex
            return( bseq)
        else :
            bseq += sex


def wseek( ) :
    bseq=""
    while(1) :
        sex = birth()
        if sex == 'F' :
            bseq += sex
            return( bseq)
        else :
            bseq += sex

total= 0
for w in range( 1000 ) :
    onecase = wseek()
    total += len( onecase )
    if len( onecase) >= 6 :
        print(f' {w:5d}, {onecase}')


total= 0
print("남자를 낳을 떄 까지 가보자")
for w in range( 1000 ) :
    onecase = manseek()
    total += len( onecase )
    if len( onecase) >= 6 :
        print(f' {w:5d}, {onecase}')

