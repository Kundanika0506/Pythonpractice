# num = 145
# strNum = str(num)
# sum = 0
# for i in strNum:
#     factorial = 1
#     for j in range(1,int(i)+1):
#         factorial= factorial*j
#     sum = sum+factorial
# print(sum)
# if(sum == num):
#     print(f"{num} is a Strong number")
# else:
#     print(f"{num} is not a strong number")


def isArmstrong(num):
    strNum = str(num)
    sum = 0
    for i in strNum:
      factorial = 1
      for j in range(1,int(i)+1):
         factorial= factorial*j
      sum = sum+factorial
    if(sum == num):
        print(f"{num} is a Strong number")

for i in range(1,200):
    isArmstrong(i)
