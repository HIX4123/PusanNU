
# Recursive definition of function factorial


def factorial( number ):
   if number <= 1:   # base case
      return 1
   else:
      return number * factorial( number - 1 )  # recursive call

for i in range( 11 ):
   print("%2d! = %d" % ( i, factorial( i ) ))

def fibonacci( n ):
   if n == 0 or n == 1:  # base case
      return n
   else:                 # two recursive calls
      return fibonacci( n - 1 ) + fibonacci( n - 2 )

number = int( input( "Enter an integer: " ) )

if number > 0:
   result = fibonacci( number )
   print("Fibonacci(%d) = %d" % ( number, result ))
else:
   print("Cannot find the fibonacci of a negative number")


