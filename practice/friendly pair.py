num1= 6
num2= 28

def Factors(num):
    sum = 0
    for i in range(1,num):
        if(num%i==0):
            sum+=i
    return sum/num
    
if(Factors(num1)== Factors(num2)):
    print(f"{num1} and {num2} are Friendly pairs")
else:
    print(f"{num1} and {num2} are not friendly pairs")