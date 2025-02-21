num = 12321
if(num==int(str(num)[::-1])):
    print(f"{num} is a Palindrome number")
else:
    print(f"{num} is not a palindrome number")