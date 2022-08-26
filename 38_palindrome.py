
num=int(input("Enter number:"))
temp=num
rev=0
digit = 0
while(num >0):
    dig= num % 10
    rev=rev*10+dig
    num //= 10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome!")


# num=input("Enter number:")
# print(num)
# rev = num[::-1]

# if num != rev:
#     print(num,"Is not palindrome")
# else:
#     print(num,"Is palindrome")