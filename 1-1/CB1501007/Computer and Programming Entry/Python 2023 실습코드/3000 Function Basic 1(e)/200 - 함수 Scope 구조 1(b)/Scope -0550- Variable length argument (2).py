
# 디폴트 매개변수 넘겨주기와 가변길이의 변수 넘겨주기
# 만일 우리가 넘겨줄 변수의 갯수를 모른다고 할 경우 유용하다.



print("\n 실험 12 - 가변길이의 argument passing")
def printinfo2( arg1, *vartuple ):
   print("Output is: ")
   print("arg1=%d 추가 변수의 갯수 = %d" % (arg1, len(vartuple)))
   for var in vartuple:
      print(var)
   return;

# Now you can call printinfo function
printinfo2( 10 );
printinfo2( 70, 60, 50 );



# 매개변수가 반드시 하나 이상 들어올 때
# 처음 매개변수는 num1, 나머지는 튜플에 저장
def VarargFunc(num1, *nums):
    print(num1, nums)

VarargFunc(1, 2, 3, "bababa")




