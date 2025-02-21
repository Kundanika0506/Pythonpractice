num =int(input("Enter a number: "))
sum = 0
for i in range(1,num+1):
    sum += i
    print(sum)

'''num1 = 86
num2 = 40
num3 = 16
if(num1 > num2 and num1 > num3):
    print(f"the greatest number is {num1}")
elif(num2 > num1 and num2> num3):
    print(f"the greatest number is {num2}")
else:
    print(f"the greatest number is {num3}")

x = 2 
if(x%2 == 0):
    print(f"{x} is even")
else:
    print(f"{x} is odd")

name = "Kundanika"
vowels = "aeiouAEIOU"
count = 0
for i in name:
    if i in vowels:
        count += 1
print(count)

gmail = "kundanika.madireddy234"
if(gmail.endswith("@gmail.com")):
    print(f"{gmail} is a valid mail ID")
else:
    print(f"{gmail} is not a valid gmail ID")

num = int(input())
for i in range(1, num+1):
    if(num%i == 0):
        print(i)

num = int(input())
ans = 1
for i in range(1, num+1):
    ans *= i
print(ans)

name = input("enter your name ")
count = 0 
for i in name:
    count += 1
print(count)

name = "Kundanika Madireddy"
ans = name[:: -1]
print(ans)

name = "KundANIka"
ans = name.swapcase()
print(ans)'''
