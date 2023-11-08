import time
import math



N = 1000000
start = time.process_time()
for i in range( N ) :
    a = 109813.0*1023801.2*i

delta = time.process_time() - start     # end
print(f" 1. a =, {delta:6.3f} milli." )

start = time.process_time()
for i in range( N ) :
    a = 109813.0*1023801.2*i
    b = a*a*a

delta = time.process_time() - start     # end
print(f" 2. a*a*a =, {delta:6.3f} milli." )

start = time.process_time()
for i in range( N ) :
    b = math.sqrt( i )


delta = time.process_time() - start     # end
print(f" 3. math.log(a) =, {delta:6.3f} milli." )



