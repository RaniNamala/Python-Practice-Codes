#In this code we achieving Polymorphism
#Using Method Overridding
class Calculator:
    def calculate(self,a,b):
        pass

class Add(Calculator):
    def calculate(self, a, b):
        print('Addition:',a+b)

class sub(Calculator):
    def calculate(self, a, b):
        print('Subtraction:',a_b)

class Mul(Calculator):
    pass

ref = Add()
ref.calculate(10,20)

ref = Sub()
ref.calculate(20,10)

ref = Mul()
ref.calculate(10,20)