num=int(input("Enter n :- "))
for i in range( 1 , num + 1 ):
    for j in range( num - 1, i , - 1):
        print(" ",end="")
    for j in range( 1, i + 1):
        print("X",end=" ")
    print( )


# n=int(input("Enter n :- "))
# for i in range (1,n+1):
#     for j in range (1,i+1):
#         print("*",end=" ")
#     print()

# num=int(input("Enter num :- "))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(1,end=" ")
#     print()
    
num=int(input("Enter num :- "))

for i in range(num):
    print(" " * (num - i), "*" * (2 * num + 1))
for i in range(num - 2, -1 , -1):
    print(" " * (num - i), "*" * (2 * num + 1))
