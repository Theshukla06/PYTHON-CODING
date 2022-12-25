# def Decimal(num):
#     if num >= 1:
#         Decimal(num // 2)
#         print(num%2, end=" ")
# num =10
# Decimal(num)

# arr = []
# num = int(input("Enter num :- "))
# for i in range(0,num):
#     arr1 = int(input())
#     arr.append(arr1)
# sum = 0
# for arr1 in arr:
#     sum = sum + arr1
# print("Result :- ",sum)

# arr = [1,2,3,4,5,1,2,3,6,7,8,6]
# for i in range (0,len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] == arr[j]:
#             print(arr[j], end=" ")
# str = " Hy i am ankit "
# str1 = str[::-1]
# print(str1)

# def ChangeAds(b):
#     num_bin = bin(b)[2:]
#     ind_1 = num_bin.index("1")
#     num_bin = num_bin[ind_1]
#     invert_bin=""
#     for i in num_bin:
#         if i == '1':
#             invert_bin += '0'
#         else:
#             invert_bin += '1'
#     return int(invert_bin,2)