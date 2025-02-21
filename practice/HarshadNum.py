num = 21
strNum= str(num)
sum = 0
for i in strNum:
    sum+= int(i) 
print(sum)
if(num%sum==0):
    print(f"{num} is a Harshad number")
else:
    print(f"{num} is not a Harshad number")