
# 전역변수와 지역 변수

total = 0 ; # This is global variable.
count = 0 ;

def sum( arg1, arg2 ):  # Add both the parameters and return them."
   global count          # 이것을 빼고 한번 계산해 보시오.
   total = arg1 + arg2; # Here total is local variable.
   print("Inside the function local total : ", total)
   count += 1
   return total;

# Now you can call sum function
sum( 10, 20 );
print("Outside the function global total : ", total)


# argument
