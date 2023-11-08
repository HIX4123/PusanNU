#-------------------------------------------------------------------------------
# Purpose:     Zoh's Work     "過猶不及"
#-------------------------------------------------------------------------------

# Sort by grade then by age
from operator import itemgetter
L = [('Bob', 'B', 30),
	 ('Sam', 'A', 35),
     ('Max', 'B', 25),
     ('Tom', 'A', 20),
	 ('Sam', 'B', 32),
     ('Max', 'C', 15),
     ('Tom', 'B', 28),
     ('Ron', 'A', 40),
     ('Ben', 'B', 15)]
Lx = sorted(L, key=itemgetter(1,2))

for w in Lx :
    print(w)