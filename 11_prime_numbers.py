# PRIME NUMBER

num = int(input('Enter a number :-'))
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(num,'Is Not Prime')
            break
    else:
        print(num,"Is Prime Number")
else:
    print(num,"Is Not Prime Number")
   











# # # # #Write a program to find series of prime numbers from 100 to 200 using for-else loop.

# # # # # lower=int(input("Enter Lower Number :- "))
# # # # # upper=int(input("Enter lower Number :- "))

# # # # # for num in range(lower , upper+1 ):
# # # # #     for i in range (2,num):
# # # # #         if (num%i)==0:
# # # # #             break
# # # # #     else:
# # # # #         print(num)

# # # # num=int(input("Enter a  Number :- "))
# # # # # If number is greater than 1
# # # # if num > 1:
# # # #    # Check if factor exist  
# # # #    for i in range(2,num):
# # # #        if (num % i) == 0:
# # # #            print(num,"is not a prime number")
# # # #            break
# # # #    else:
# # # #        print(num,"is a prime number")
# # # # # Else if the input number is less than or equal to 1
# # # # else:
# # # #    print(num,"is not a prime number")   



# # # lower=int(input("Enter a lower number :- "))
# # # upper=int(input("Enter a upper number :- "))

# # # for num in range (lower,upper+1):
    
# # #     for i in range(2,num):
# # #         if(num % i )==0:
# # #             break
# # #     else:
# # #         print(num)



# # lower=int(input("Enter a lower no :- "))
# # upper=int(input("Enter a upper no :- "))

# # for num in range (lower,upper+1):

# #     for i in range(2,num):
# #         if(num % i )==0:
# #             break
# #     else:
# #         print(num)

# lower=int(input("Enter a lower number :- "))
# upper=int(input("Enter a upper number :- "))

# for num in range(lower,upper+1):
#     for i in range (2,num):
#         if(num % i)==0:
#             break
# #     else: 1
# #        print(num)


# num=int(input("Enter a number :- "))

# if num > 1:
   
#     for i in range (2,num):
   
#        if( num % i)==0:
#           print(num,"is not prime no")
#           break
   
#     else:
#         print(num,"is a prime no")

# n=int(input('enter :-'))
# if n > 0:
#     for i in range(2,n):
#         if n % i == 0:
#             print('not prime')
#             break
#         else:
#             print('prime')

# num = int(input('Enter a no :-'))
# if num > 1:
#     for i in range(2,num):
#         if num % i == 0:
#             print("is not prime")
#             break
#     else:
#         print(num,"is prime")
# else:
#     print('Not prime')
# num = int(input("Enter Number :- "))
# if num > 1 :
#     for i in range (2,num):
#         if num % i == 0:
#             print(num,"Is Not Prime Number")
#             break
#     else:
#         print(num,"Is Prime Number")
# else:
#     print(num,'Is Not Prime Number')


# num=int(input("Enter a  Number :- "))
# # If number is greater than 1
# if num > 1:
#    # Check if factor exist  
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            break
#    else:
#        print(num,"is a prime number")
# # Else if the input number is less than or equal to 1
# else:
#    print(num,"is not a prime number")