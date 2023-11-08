
# 디폴트 매개변수 넘겨주기와 가변길이의 변수 넘겨주기
# 만일 우리가 넘겨줄 변수의 갯수를 모른다고 할 경우 유용하다.


print("\n 실험 11 - Default Argument Setting ")
def printinfo1( name, age = 35 ):
   print("Name: ", name);
   print("Age ", age);
   return;

# Now you can call printinfo function
printinfo1( age=50, name="miki" );
printinfo1( name="miki" );


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



