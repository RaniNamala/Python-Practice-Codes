'''Access Modifiers/sp
To determine the accessibility of data members and member function.'''
'''public ---> variable_name
private ----->__variable_name
protected------> __variable_name
public = It should be accessed inside the class, outside the class.
Protected = It should be accessed inside the same class in which
we have declared and inside child class.
Private = It should be accessed inside the same class in which we declared '''

class Demo1:
    def __init__(self,name):
        self.firstname = name
    def disp1(self):
        print(self.firstname)
d1 = Demo1('Akash')
print(d1.firstname)
d1.disp1()

class Demo2(Demo1):
    def disp2(self):
        print(self.firstname)
d2 = Demo2('Pooja')
print(d2.firstname)  
d2.disp2()    

'''
The variables which are public, can be accessed inside the
same class, outside of any class, inside the child class,
inside non-child class.
'''