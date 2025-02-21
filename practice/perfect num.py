# num = 6
# sum = 0
# for i in range(1,num):
#     if(num%i==0):
#         sum += i
# if(sum==num):
#     print(f"{num} is a perfect number")
# else:
#     print(f"{num} is not a perfect number")



def isPerfect(num):
    sum = 0
    for i in range(1,num):
        if (num%i==0):
            sum+=i
    if(sum==num):
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")

for i in range(1,50):
    isPerfect(i)