# # def conditional(num1,num2):
# #     if num1>num2:
# #         print("10 bada h 5 se")
# #     else:
# #         print("5 chota h 10 se")
# # num1= 10
# # num2 = 5
# # conditional(num1,num2)
# # pmt = 'I have done my work .
# # '
# # print("Enter Your Name :- ")
# # pmt = input("Enter Your Name :- ")
# # pmt = input("Enter Your college name :- ")
# # print(pmt)
# # if 'Ankit' in pmt:
# #     print('********Yes your name is correct********')
# # else:
# #     print('********Your name is not correct Error********')

# def name(nam1):
#     if 'Ankit' in nam1:
#         print('Yes your name is correct')
#     else:
#         print('Your name is not correct Error')

# nam1 = input("Enter Your  Name :- ")
# name(nam1)

# def college(nam2):
#     if 'Medi' in nam2 :
#         print('Yes your college name is correct')
#     else:
#         print('Your name is not correct Error')

# nam2 = input("Enter Your College Name :- ")
# college(nam2)

# list = ["Ankit","Ankit","Shukla"]
# for i in list:
#     print(i,end="\n")

# x =list.count("Ankit")
# print(x,"Times in your list")


# print("*****************")



list = ["Buy a I-bus ticket", "Buy a cold drink", "Spend money for lunch", "Bought chocolate for sister", "Spend money for fruits", "Buy a I-bus ticket", "Spend money for lunch", "Bought chocolate for sister", "Bought chocolate for sister","Buy a I-bus ticket", "Spend money for fruits", "Spend money for lunch","Buy a I-bus ticket"]
count=0
dict={}
for i in range(len(list)):
    j=i+1
    for j in range(len(list)):    
            if list[i]==list[j]:
                count = count+1
    if count>=1 and count<=5:
            dict[list[i]]=count
    count=0
print(dict)

# def NumOfTimes(list):
#     count = 0
#     dict = {}
#     for i in range(len(list)):
#         j=i+1
#         for j in range(len(list)):
#             if (list[i]==list[j]):
#                 count = count+1
#         if count>=1 and count<=5:
#             dict[list[i]]=count
#     count=0

# list = ["Buy a I-bus ticket", "Buy a cold drink", "Spend money for lunch", "Bought chocolate for sister", "Spend money for fruits", "Buy a I-bus ticket", "Spend money for lunch", "Bought chocolate for sister", "Bought chocolate for sister","Buy a I-bus ticket", "Spend money for fruits", "Spend money for lunch","Buy a I-bus ticket"]
# NumOfTimes(dict)



# l1 = list.count('Buy a cold drink')
# print('The count of Buy a cold drink is:',l1)

# l2 = list.count('Buy a I-bus ticket')
# print('The count of Buy a I-bus ticket is:',l2)


# print('The count of Spend money for lunch is:', count)
# count = vowels.count('Spend money for lunch')

# print('The count of Bought chocolate for sister is:', count)
# count = vowels.count('Bought chocolate for sister')

# print('The count of Buy a cold drink is:', count)
# count = vowels.count('Buy a cold drink')


# dict = { }
# print(dict)
# my_dict = {"Name":[],"Address":[],"Age":[]};

# my_dict["Name"].append("Ankit")
# my_dict["Address"].append("Shukla")
# my_dict["Age"].append(22)	
# print(my_dict)

# list = ["Ankit","Ankit","Shukla"]
# list.append("Pandit")
# print(list)