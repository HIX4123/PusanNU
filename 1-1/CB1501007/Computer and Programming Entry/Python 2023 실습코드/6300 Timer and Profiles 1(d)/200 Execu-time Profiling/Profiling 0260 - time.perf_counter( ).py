from datetime import datetime
import time # clock은 Python 3.8에서는 더 이상 지원하지 않음

t = datetime.utcnow()
print ('t == %s    %s\n\n' % (t,type(t)))

n = 100000

te = time.perf_counter()
for i in range(2):
    t_stripped = t.strftime('%Y%m%d%H%M%S%f')

print ("1. ", time.perf_counter() -te)
print (t_stripped," t.strftime('%Y%m%d%H%M%S%f')")

print

te = time.perf_counter()
for i in range(1):
    t_stripped = str(t).replace('-','').replace(':','').replace('.','').replace(' ','')
print ("2. ", time.perf_counter() -te )
print (t_stripped," str(t).replace('-','').replace(':','').replace('.','').replace(' ','')")

print

te = time.perf_counter()
for i in range(n):
    t_stripped = str(t).translate(' -:.')

print ("3. ", time.perf_counter() -te )
print (t_stripped," str(t).translate(None,' -:.')")

print

te = time.perf_counter()
for i in range(n):
    s = str(t)
    t_stripped = s[:4] + s[5:7] + s[8:10] + s[11:13] + s[14:16] + s[17:19] + s[20:]
print ("4. ", time.perf_counter() -te )
print ( t_stripped," s[:4] + s[5:7] + s[8:10] + s[11:13] + s[14:16] + s[17:19] + s[20:] ")