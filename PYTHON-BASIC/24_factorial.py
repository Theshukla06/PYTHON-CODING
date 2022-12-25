# from math import factorial


# num = int(input('Enter Any  Number :-'))
# factorial = 1
# if num  <= 0 :
#   print('Enter Greater Then 0')
# else:
#   for i in range(1,num+1):
#     factorial = factorial * 1
#     break
#     print('Your Factorial Ans is :-',factorial)







# # num=int(input("Enter a number :- "))
# # factorial=1
# # # if num <= 0:
# # #     print("Enter greator then 0 ")
# # # else:
# # for i in range(1,num+1):
# #    factorial=factorial*i
# #    print("Factorial :- ",factorial)

# a=int(input ("Enter a number :- "))
# fact=1
# while(a > 0):
#   fact=fact * a
#   a = a - 1
# print("Factorial :- ",fact)


# def Fact(num):
#   fact = 1
#   for i in range(1,num+1):
#     fact = fact * i
#   return fact

# a = int(input("Enter a number :- "))
# print(Fact(a))

def Factorial(num):
  fact = 1
  for i in range(1,num+1):
    fact = fact*i
  return fact
num = int(input("Enter a number :- "))
print(Factorial(num))



