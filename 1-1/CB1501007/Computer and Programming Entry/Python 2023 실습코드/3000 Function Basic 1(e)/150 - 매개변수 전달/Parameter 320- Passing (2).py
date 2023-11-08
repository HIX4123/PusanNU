
def changeme( mylist ):
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return

def changeme2( mylist ):
   mylist = [-11,-22,-33,-44]; # 완전히 새로 구성함
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

