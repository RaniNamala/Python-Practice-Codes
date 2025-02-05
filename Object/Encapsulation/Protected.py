class Demo1:
    def __init__(self,name):
        self._firstname = name #Protected Variable
    def disp1(self):
        print(self._firstname)
d1 = Demo1('Rani')
print(d1._firstname)
d1.disp1()

class Demo2(Demo1):
    def disp2(self):
        print(self._firstname)
d2 = Demo2('Macha')
print(d2._firstname)  
d2.disp2()   

class Demo3:
    def disp3(self):
        print(d1._firstname)
d3 = Demo3()
d3.disp3()        


'''
The variables which are Protected, can be accessed inside the
same class, outside of any class, inside the child class,
inside non-child class.

The variables which are Protected should be accessed
in side the same class and inside the child class and 
this is programmers duty to follow these rules.
'''