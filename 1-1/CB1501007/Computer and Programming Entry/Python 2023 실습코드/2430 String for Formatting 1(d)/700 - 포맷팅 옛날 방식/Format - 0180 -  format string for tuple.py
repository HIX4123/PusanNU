#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

thetuple = (1, 2, 3)

#print ("this is a tuple: %s" %  thetuple ) # 오류

print (" %s  %s  %s" % (1, 2, 3) )
print ("this is a tuple: %s" % (thetuple,) ) # 통으로 출력하기


tup = (1,2,3)
print( "First: %d, Second: %d, Third: %d" % tup )
print( 'First: {}, Second: {}, Third: {}'.format(1,2,3)) # 나쁜 방
print (f'First: {tup[0]}, Second: {tup[1]}, Third: {tup[2]}')

