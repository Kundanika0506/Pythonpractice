# num= 371
# strNum= str(num)
# length = len(strNum)
# sum=0
# for i in strNum:
#     sum+= int(i)**length
#     print(sum)
# if(sum==num):
#     print(f"{num} is an Armstrong number")
# else:
#     print(f"{num} is not an armstrong number")


#armstrong number withing a range

def isArmstrong(num):
    strNum= str(num)
    length = len(strNum)
    sum=0
    for i in strNum:
        sum += int(i)**length
    if(sum==num):
         print(f"{num} is an Armstrong number")


for i in range(100,2000):
     isArmstrong(i)    
