class Employ:
    def __init__(self,Name):
        print('Constructor is call')
        self.Name = Name

    def __del__(self):
        print('Destructor is call',self.Name)

    def Display(self):
        print("Your Name Is :- ",self.Name)
    
obj_Ankit = Employ("Ankit Shukla")
obj_Ankit.Display()

obj_Atul = Employ("Atul Shukla")
obj_Atul.Display()

del obj_Ankit
print("I'Am Destructor Destroy Ankit")