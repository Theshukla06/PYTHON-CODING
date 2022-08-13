from unicodedata import name


class StudentData:
    def SetData(Self):
        Self.name = input('Enter Your Name :- ')
        Self.age = int(input('Enter Your Age :- '))
        Self.per = float(input('Enter Your Percentage :- '))
    
    def Display():
        print('Your Name is :- ',name)
        print('Your Age is :- ',age)
        print('Your Percentage is :- ',per)


