# num = int(input('Enter Any Number :- '))
# for i in range(0,num):
#     for j in range(i+1):
    
#         print('*',end=" ")
    
#     print()


# num = int(input('Enter Any Number :- '))
# for i in range(0,num+1):
    
#     for j in range(0,num-i-1):
#         print(end=" ")
        
#     for j in range(0,i+1):
#         print('*',end=" ")
    
#     print()

def Pyramid(num):
    for i in range(0,num+1):
    
        for j in range(0,num-i+1):
            print(end=" ")
        
        for j in range(0,i+1):
            print('*',end=" ")
        print()
n = int(input('Enter Any Number :- '))
print(Pyramid(n))




# for i in range(0,num):
    #     for j in range(i+1):
    #         print('*',end=" ")
    
    #     print()