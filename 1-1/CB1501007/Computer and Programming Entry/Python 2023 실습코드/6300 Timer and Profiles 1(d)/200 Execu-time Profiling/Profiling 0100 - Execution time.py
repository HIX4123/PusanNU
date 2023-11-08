# time.clock( )은 더이상 지원되지 않습니다. 2021년 3월 봄날에


import time

N = 1000000

mstart = time.process_time()
for i in range( N ) :  # 시간을 측정하고자 하는 code
    a = 109813.0*1023801.2*i

mend = time.process_time()
delta = mend - mstart     #
print("Ellasped =", delta, " milli." )


start = time.process_time()
for i in range( N ) :
    a = 109813.0*1023801.2*i
    b = a*a*a

delta = time.process_time() - start     # end�뿉 肄붾뱶媛� 援щ룞�맂 �떆媛� ����옣
print("Ellasped =", delta, " milli." )



