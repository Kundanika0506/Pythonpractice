num = 5
# fact = 1
# for i in range(1,num+1):
#     fact = fact*i
# print(f"Factorial of {num} is {fact}")

#using recursion:

def getFactorial(num):
    if num==0:
        return 1
    
    return num*getFactorial(num-1)

fact = getFactorial(num)
print(f"the factorial of {num} is {fact}")