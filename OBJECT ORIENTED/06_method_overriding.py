# METHOD OVERRIDING ---->

class Parent():
    def Add(self):
        print("A")
class Child(Parent):
    def Add(self):
        print("B")
        

obj = Child()
obj.Add()
