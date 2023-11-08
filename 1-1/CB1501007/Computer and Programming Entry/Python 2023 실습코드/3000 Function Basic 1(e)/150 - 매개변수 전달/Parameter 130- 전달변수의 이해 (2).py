# Purpose: 함수에 변수를 어땋게 넘길 것인가
# Python에서는 function에 넘겨주는 parameter(argument)는
#  name, object 라고 한다. (variable, value나 reference가 아니라..)
#!/usr/bin/env python
#-------------------------------------------------------------------------------


def changeme( mylist ):         # list는 object를 넘거주는 것임
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return

def changeme2( mylist ):
   mylist = [-11,-22,-33,-44];  # 완전히 새로 구성함, name만 사용
                                # 새로운 list를 만들고 이것을 mylist가 지정
   print("Values inside the function: ", mylist)
   return

def printinfo( name, age ):
   print("Name: ", name , "\tAge ", age);
   return;


print("\n 실험 1 - parameter Passing \n")

mylist = [10,20,30];
changeme( mylist );


print("Values outside the function: mylist = ", mylist)
print("\n 실험 2 - parameter Passing \n")

# Function definition is here

yourlist = [10,20,30];
changeme2( yourlist );
print("Values outside the function: mylist2= ", yourlist)


print("\n 실험 3 - 매개변수 전달하기 \n")


# Now you can call printinfo function
printinfo( age=50, name="miki" );
printinfo( 23, "Elizabeth")
printinfo( "Michael", 31 )
# printinfo( name="miki" );
# printinfo(  );

