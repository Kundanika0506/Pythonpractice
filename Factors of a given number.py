# num= int(input("Enter a number: "))
# for i in range(1,num+1):
#     if(num%i==0):
#         print(i)

# def giveFactors(*num):
#     for number in num:
#         for i in range(1,number+1):
#             if(number%i==0):
#                 print(i)

        
# giveFactors(8,6,4,9)
# # giveFactors(16)


# def sumofFactors(num):
#     sum=0
#     for i in range(1,num):
#         if(num%i==0):
#             sum+= i
#     return sum/num

# if(sumofFactors(6)==sumofFactors(28)):
#     print("Friendly pair")
# else:
#     print("Not a friendly pair")



emails= ["kundan@gmail.com","Kundan@outlook.com", "Uday@outlook.com"]
for i in emails:
    if(i.endswith("@outlook.com")):
        print(i)

strNum ="Uday"
if(strNum==strNum[::-1]):
    print("palindrome")
else:
    print("not a palindrome")

names= ["Dad", "Mom", "kundan", "level"]
for i in names:
    if(i.lower()==i.lower()[::-1]):
        print(i)

# nums = [3,4,5,6,2,8,1,9,7,10,21,14,15,28,32,35,40,47,54]
# sum =0 
# for i in nums:
#     sum+=i
# print(sum)
# sum=0

# for i in nums:
#     if(i%2==0):
#         sum+=i
# print(sum)

# def isPrime(number):
#     count=0
#     for i in range(1,number+1):
#         if(number%i==0):
#             count+= 1
#     return count==2
# for i in nums:
#     if(isPrime(i)):
#         print(i)
        

