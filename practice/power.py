num1 = 2
num2 = 3
def power(num1,num2):
    if num2!=0:
        return num1 * power(num1, num2-1)
    else:
        return 1
    
print(f"{num1} to the power {num2} is {power(num1,num2)}")