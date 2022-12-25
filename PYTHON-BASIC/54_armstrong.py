#  ARMSTRONG NUMBER CHECK

number = int(int(input("Enter a no :- ")))
temp = number
sum = 0
# rev = 0
digit = 0

while (temp > 0):
# while (num > 0):
    digit = temp % 10
    # digit = num % 10
    sum += digit ** 3
    #rev = rev * 10 + digit
    temp //= 10
    # num //= 10

if number == sum:
# if tem == rev:
    print(number,"IS Armstrong Number")
else:
    print(number,"IS Not Armstrong Number")
    





# num = int(input("Enter a three number :- "))
# temp = num 
# sum = 0
# digit = 0

# while temp > 0:
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10

# if num == sum:
#     print(num,"Is Armstrong Number")
# else:
#     print(num,"Is Not Armstrong Number")
    