num = 12
sum = 0
for i in range(1,num):
    if(num%i==0):
        sum+=i
if(sum>num):
    print(f"{num} is an abundant number")
else:
    print(f"{num} is not an abundant number")