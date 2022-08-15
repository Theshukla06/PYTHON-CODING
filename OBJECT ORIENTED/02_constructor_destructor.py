class Student:
    # TO GET STUDENT INFORMSTION
    schoolName = "S.V.M School"
    rollNo = 786
    Name = "Ankit"

    def __init__(self,Name,rollNo,schoolName):
        self.rollNo = rollNo
        self.Name = Name
        self.schoolName = schoolName
        print('Value Set')
    
    def DisplayStudentData(self):
        print("Student Name is :- ",self.Name)
        print("Student Roll No is :- ",self.rollNo)
        print("Student School Name is :- ",self.schoolName)


print(Student.Name)
print(Student.rollNo)
print(Student.schoolName)

obj1 = Student("Ankit Shukla",21501023,"Medicaps University, Indore")
obj1.DisplayStudentData()

obj2 = Student("Atul Shukla",23215010,"DAVV University, Indore")
obj2.DisplayStudentData()