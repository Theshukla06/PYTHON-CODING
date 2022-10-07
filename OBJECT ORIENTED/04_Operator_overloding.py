class OperatorOverloding:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self,other):
        return self.a + other.a , self.b + other.b

ob1 = OperatorOverloding(5,5)
ob2 = OperatorOverloding(5,5) 

ob3 = ob1+ob2
print(ob3)

