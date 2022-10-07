# SINGLE INHERITANCE

# class A:
#     def DisplayA(self):
#         print("Hy i am in A")
# class B(A):
#     def DisplayB(self):
#         print("Hy i am in B")

# obj = B()
# obj.DisplayA()
# obj.DisplayB()


# MULTIPLE INHERITANCE

# class Top:
#     def TopA(self):
#         print("Hello I'Am in Top class A")
# class Mid:
#     def MidA(self):
#         print("Hello I'Am in Mid class A")
# class Low(Top,Mid):
#     def LowA(Self):
#         print("Hello I'Am in Low class A")

# obj = Low()
# obj.TopA()
# obj.MidA()
# obj.LowA()


class Bus:
    def Eicher(BigBus):
        print("Hello I'am Eicher BigBus")
class Car:
    def Tata(Baleno):
        print("Hello I'am Tata Car Baleno")
class Bike(Bus,Car):
    def Honda(Activa):
        print("Hello I'am Hona Activa")


obj = Bike()
obj.Honda()
obj.Eicher()
obj.Tata()

