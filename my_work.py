# a=int(input('enter a'))
# b=int(input('enter b'))
# sum=a+b
# print(sum)

# def sum(a,b):
#     return a+b

# a=int(input('enter a'))
# b=int(input('enter b'))

# a1=sum 
# print(a1)

# n=int(input("enter number"))
# for i in range(1,11):
#     print(n,"X",i,"=",n*i)
    
#     # table=n*i
#     # print("*"i="table")
# num = int(input("Enetr a no :-"))
# if num % 2 == 0:
#     print('prime no')

# else:
#     print('not prime no')

# a="Shukla"
# print(type(a))
# n=int(a)
# print(type(n))

# for i in range (1,10+1):
#     print(i)

# x='2'

# print(x)
# x=int(x)
# print(type(x))

# #BOOLEAN
# a= 5
# b= 10
# c= a<b
# print(c)
# def Sum(a,b):
#     print('value A is :-',a)
#     print('value B is :-',b)
#     return a + b

# x= int(input("Enter A Value :- "))
# y= int(input("Enter B Value :- "))
# s=Sum(x,y)
# print(s)

# #EVEN OR ODD NO PROGRAM
# def Even_Odd(a):
#     if a%2==0:
#         print("Your no is Even :-",a)
#     else:
#         print("Your no is Odd :-",a)
# x=int(input('Enter Value A :-'))
# y=Even_Odd(x)

# def Factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact * i
#         return fact
# a=int(input('Enter a :- '))
# b=Factorial(a)
# print('Your Factorial Ans is :-',b)

# from unicodedata import name


# class Student:
#     def setdata(self):
#         self.name=input('Enter Your Name :-')
#         self.age=int(input('Enter Your Age :-'))
#         self.colour=input('Enter Your Color :-')
#     def display(self):
#         print('Name :- ',self.name)
#         print('Age :- ',self.age)
#         print('Colour :- ',self.colour)
# a=Student()
# a.setdata()
# a.display()

# l=[1,'x',22,'a']
# print(l)
# l1=[x for x in l if type(x)==int]
# print(l1)

# l2=[x for x in l if type(x)==str]
# print(l2)

# def remove(string):
#     return string.replace(" ","")

# a="Hy my name is ankit shukla"
# print(remove(a))



#  PROGRAMIZ
# Q1
# print('Hello World!')

# Q2
# a = int(input('Enter 1st no :- '))
# b = int(input('Enter 2nd no :- '))
# add = a + b 
# print("Your or ans is ",add)


# Q3
# num = int(input('Enter no :- '))
# squr_root = num ** 0.5
# print('Your Square root ans is :-',squr_root)

# Q4
# def AreaOfTriangle(base,height):
#     print('Your Base Value is :- ',base)
#     print('Your Height Value is :- ',height)

#     return base * height / 2

# Base = int(input('Enter Base Value :- '))
# Height = int(input('Enter Height Value :- '))

# print("Your Ans Is :- ",AreaOfTriangle(Base,Height))


# Q5
#  Quadratic Equation
# import cmath
# a = int(input('Enter 1st no :- '))
# b = int(input('Enter 2nd no :- '))
# c = int(input('Enter 3rd no :- '))

# # d = (b ** 2) - (4 * a * c )
# # FIND SOLUTION
# sol1 = - b - cmath.sqrt((b ** 2) - (4 * a * c )) / 2 * a
# sol2 = - b + cmath.sqrt((b ** 2) - (4 * a * c )) / 2 * a

# print(sol1,sol2)

# Q6
# SWAP TWO VARIABLES
# x = 5
# y = 6

# tem = x
# x = y 
# y =  tem

# print('x after swap',x)
# print('y after swap',y)

# Q7
# RANDOM NUMBER
# import random
# print(random.randint(0,9))

# Q8
# CHECk NUMBER IS POSITIVE NUMBER OR NEGATIVE
# EXAPLE (1) POSITVE NUMBET (-1) IS NEGATIVE NUMBER
# a = int(input('Enter 1st no :- '))
# if a > 0:
#     print('Number is positive number')
# elif a == 0:
#     print('Number is less then zero')
# else:
#     print('Number is negative number')


# Q9
# CHECK EVEN OR ODD
# a = int(input('Enter 1st no :- '))
# if a % 2 == 0 :
#     print('Number is even')
# else:
#     print('Number is odd')

# def EvenOdd(num):
#     if num % 2 == 0:
#         return print(num,'is Even')
#     else:
#         return print(num,'is Odd')

# num = int(input('Enter a number :- '))
# EvenOdd(num)


# Q10
# PRIME NUMBER
# num = int(input('Enter no :- '))
# for i in range(2,num):
#     if num % i == 0:
#         print('Not Prime')
#         break
# else:
#     print("Prime No")

# def Prime(num):
#     for i in range (2,num):
#         if num % i == 0:
#            print('not prime')
#            break
#     else:
#         print('prime')

# num = int(input('Enter a number :-'))
# Prime(num)

# Q16
# FACTORIAL OF A NUMBER 
# num = int(input('Enter a number :- '))
# factorial = 1
# if num < 0:
#     print('Enter Greater Number')
# elif num == 0:
#     print('The Factorial of 0 is 1')
# else: 
#     for i in range(1,num+1):
#         factorial = factorial * i
#         print('Your Factorial Ans :- ',factorial)
    
# def Factorial(num):
#     factorial  = 1
#     for i in range(1,num + 1):
#         factorial = factorial * i
#         print('Your Factorial Ans :- ',factorial)
        
# num = int(input('Enter a factorial num :- '))
# Factorial(num)


# Q17
#  MULTIPLICATION TABLE
# num = int(input('Enter a num :- '))
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)

# def Multiplication(num):
#     for i in range(1,11):
#         print(num,"x",i," = ",num*i)
# num = int(input('Enter Multiplication Number :- '))
# Multiplication(num)

# Q18
# FIBONACCI SEQUENCE
# def fibo(num):
#     if num == 1:
#         return 0
#     elif num == 2:
#         return 1
#     else:
#         return (fibo(num - 1) + fibo(num - 2))

# num = int(input('Enter num value :- '))
# for i in range(1,num+1):
#     print(fibo(i))

# Q19
#  SUM OF NATURAL NUMBER
# num = int(input('Enter num value :- '))
# sum = 0
# while(num > 0):
#     sum += num
#     num -= 1
#     print('Your sum value',sum)

# Q20
# POWER

# def Pow(a,b):
#     if b == 1:
#         return a
#     else:
#         return a * pow(a,b-1)
# a = int(input('Enter a value :- '))
# b = int(input('Enter b value :- '))
# print(Pow(a,b))

# Q21
# PALINDROME
# a = input('Enter a value :- ')
# reverse = a[::-1]
# if a == reverse:
#     print('Number Is Palindrome')
# else:
#     print('Number Is Not Palindrome')



# def Feb(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return (Feb(num-1)+ Feb(num-2))
# num = int(input("Enter a no :- "))
# for i in range(num):
#     print(Feb(i))

# num = input("Enter a no :- ")
# rev = num[::-1]

# if rev != num:
#     print(num,"Its Not Palindrome")
# else:
#     print(num,"Is Palindrome")

# ARMSTRONG

# num = int(input("Enter a three no :- "))
# temp = num
# sum = 0 
# digit = 0

# while temp > 0:
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10
    
# if num == sum :
#     print(num,"Is Armstrong Number")
# else:
#     print(num,"Is Not Armstrong Number")

# def Fib(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return (Fib(num - 1)+Fib(num - 2))

# num = int(input('Enter a number :- '))
# for i in range(num):
#     print(Fib(i))



# num = int(input('Enter a number :-'))
# if num > 1:
#     for i in range(2,num):
#         if num % i == 0:
#             print(num,"Number IS Not Prime")
#             break
#     else:
#         print(num,"Number Is Prime")
# else:
#     print(num,"Number Is Not Prime")


# def Fib(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return(Fib(num - 1)+ Fib(num-2))

# num = int(input("Enter a number :- "))
# for i in range(num):
#     print(Fib(i))


# num = "Ankit"
# num1 = num[::-1]
# print(num1)


# def reverse_string(str):

#     str1 = " "
#     for i in str:
#         str1 = i + str1
#     return str1

# str = "Ankit"
# print(reverse_string(str))

# a=22
# a1 = str(a)
# print(type(a1))

#LIST IN LOOP

# list = ["Ankit","Shukla","Atul","Pandit"]

# for i in list():
#     print(list)
#     break

# SUM OF NATURAL NUMBER

# num = int(input("Enter a number :- "))
# sum = 0
# for i in range(1,num + 1):
#     sum = sum + i
#     print(sum)

# num = int(input("Enter a number :- "))
# for i in range(1 , num + 1):
#     for j in range(1 , i + 1):
#         print("*",end=" ")
#     print()

# i = 4
# if i > 0:
#     pass
# while   i > 6 :
#     pass
# print("Shukla")

#SUM OF ARRAY
# arr = [1,2,3,4,5]
# sum = 0
# for i in range(0, len(arr)):
#     sum = sum + arr[i]
# print(sum)

def ShortArray(arr):
    for i in arr:
        arr.sort()
    print(arr)

arr = [7,6,4,2]
ShortArray(arr)
# arr = (7,6,4,2)
# arr.sort()
# for i in range(0, len(arr)):
#     print(arr[i], end=" ")