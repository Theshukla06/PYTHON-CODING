# def fib(n):
#     if n == 1 :
#         return 0
#     elif n == 2 :
#         return 1
#     else:
#         return(fib(n-1) + fib(n-2))

# n=int(input("Enter any number :- "))
# for i in range(1,n+1):
#     print(fib (i))



def fib(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return(fib(num - 1)+ fib(num - 2))
    
num = int(input("Enter a no :-"))
for i in range(1,num+1):
    print(fib(i))




