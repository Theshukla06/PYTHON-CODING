#                         METHOD OVERLODING
# class Student:
#     def SayHello(self,name=None):
#         if name is not None:
#             print("Hello I' Am "+name)
#         else:
#             print('Hello')
# obj = Student()
# obj.SayHello(' Ankit Shukla')


#                   METHOD OVERRIDING

class StudentFirst:
    def StudentData(self):
        print("Hy I'Am Ankit")

class StudentSecond(StudentFirst):
    def StudentData(self):
        super().StudentData(    )
        print("Hy I'Am Shukla")

obj = StudentSecond()
obj.StudentData()