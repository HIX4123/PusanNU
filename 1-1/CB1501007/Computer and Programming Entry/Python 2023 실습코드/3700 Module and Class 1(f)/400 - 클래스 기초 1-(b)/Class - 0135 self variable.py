#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-06
#-------------------------------------------------------------------------------

"""
What is the use of Self in Python?

The self is used to represent the instance of the class.
With this keyword, you can access the attributes and methods of
the class in python.
It binds the attributes with the given arguments.
The reason why we use self is that Python does not use the
‘@’ syntax to refer to instance attributes.
In Python, we have methods that make the instance to be passed
automatically, but not received automatically.
"""

class food(): # init method or constructor
    def __init__(self, fruit, color):
        self.fruit = fruit
        self.color = color

    def show(self):
        print("fruit is", self.fruit)
        print("color is", self.color )

apple  = food("apple", "red")
grapes = food("grapes", "green")

apple.show()
grapes.show()