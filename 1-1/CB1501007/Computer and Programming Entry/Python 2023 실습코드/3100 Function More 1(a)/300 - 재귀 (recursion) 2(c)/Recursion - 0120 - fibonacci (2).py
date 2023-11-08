
# 피보나치 수를 재귀적 방법으로 간단히 프로그래밍 할 수 있다.

# 단 N이 50 이상이면 엄청나게 많은 호출을 하므로 유의해야 합니다.
# 이 경우에는 리스트에 원소를 넣어서 f[i+1] = f[i] + f[i-1]과 같이
# dynamic programming으로 풀어야 합니다.

def fibonacci( n ):
   if n == 0 or n == 1:  # base case
      return n
   else:                 # two recursive calls
      return fibonacci( n - 1 ) + fibonacci( n - 2 )

number = int( input( "피보나치 수 N을 입력하시오: " ) )

if number > 0:
   result = fibonacci( number )
   print("Fibonacci(%d) = %d" % ( number, result ))
else:
   print("음수에 대한 피보나치 수는 정의될 수 없습니다.")


