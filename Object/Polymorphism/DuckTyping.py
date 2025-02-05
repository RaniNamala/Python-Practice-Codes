'''
'''

class Add:
    def calculate(self, a, b):
        print('Addition:',a+b)

class sub:
    def calculate(self, a, b):
        print('Subtraction:',a_b)

class Mul:
    pass

def permit(ref,a,b):
    if type(ref).__name__ == 'Mul':
        print('Mul Classs does Not have calculate()')
    else:    
        ref.calculate(a,b)
permit(Add(),10,20)
permit(Sub(),20,10) 
permit(Mul(),10,20)   

'''ref wont check the type of object.
ref only give importance to the calculate method.
ref only gives importance to the methods of object.
'''
#Duck Typing = Insted, it will execute an action depending on the type of built-in objects being 
#if it walks like a duck,#
