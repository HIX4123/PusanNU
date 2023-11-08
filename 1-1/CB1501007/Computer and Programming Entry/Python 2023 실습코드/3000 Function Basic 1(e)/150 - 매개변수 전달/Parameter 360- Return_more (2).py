

def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print("Inside the function : ", total)
   return total;
# ------- end of sum( ) ------------


def another( arg1, arg2, arg3, arg4 ):
   # Add both the parameters and return them."
   arg3  = arg1 + arg2
   argv  = abs(arg1 - arg2 )
   pass
   #no return value
# ------- end of another( ) ------------

def newcome( L ):
   # Add both the parameters and return them."
   L.append(  L[0] + L[1] )
   L.append( abs( L[0] - L[1] ) )
   #no return value
# ------- end of another( ) ------------

# Now you can call sum function
total = sum( 10, 20 );
print("Outside the function : ", total)

dog = cat = 222
whatdone = another(100, 200, dog, cat )
print(whatdone)
print("dog, cat = ", dog, cat)

pig = [ 100, 200 ]
newcome( pig )
print(pig)

# 실습과제
# 함수 prime_count( a,b) 는
# 정수 a부터 b까지 소수인 숫자의 갯수를 계산해서 돌려 줌
# 이것을 위해서 먼저 숫자 K가 소수인지를
# 검사하는 함수 is_prime ( K )를 먼저 작성해야 함.
