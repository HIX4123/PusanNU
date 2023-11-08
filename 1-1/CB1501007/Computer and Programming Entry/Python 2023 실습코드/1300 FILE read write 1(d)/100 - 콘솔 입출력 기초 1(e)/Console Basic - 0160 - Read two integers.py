#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     롯데 만만세
# Author:      Cho
# Created:     2021-04-09
#-------------------------------------------------------------------------------

while( True ) :
    Inline = input("Type two integers N and k:")
    N,k = map( int, Inline.split() )
    if N <=1 :
        print("We quit this work")
        break

    print(f'N={N}, k={k}')
    print("You should draw a binary tree with ord=k-1")
    print("You should draw a binary tree with ord=k ")
    print("You should draw a binary tree with ord=k+1")