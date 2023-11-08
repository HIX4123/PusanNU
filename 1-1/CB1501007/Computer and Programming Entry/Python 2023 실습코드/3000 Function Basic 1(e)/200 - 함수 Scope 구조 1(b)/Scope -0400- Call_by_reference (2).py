

def change_me( mylist ):
   mylist.append("banana");
   return


def change_you( mylist ):
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print("mylist in change_you( ) ", mylist)
   return


mylist = [10,20,30];
print("mylist before change_me( )  ", mylist)
change_me( mylist );
print("mylist after change_me( )  ", mylist)


mylist = [10,20,30];
print("mylist before change_you( )  ", mylist)
change_you( mylist );
print("mylist after change_you( )  ", mylist)