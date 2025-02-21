def isPrimeNum(num):
    count= 0
    for i in range(1,num+1):
        if (num%i==0):
            count+= 1
    if(count==2):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

for i in range(1,2001):
    isPrimeNum(i)

def add(num1,num2=3):
    print(num1+num2)
    return num1+num2
add(23,90)

def sub(num1,num2=90):
    print(num1-num2)
    return num1-num2
sub(87)    

def multiply(num1,num2):
    print(num1*num2)
    return num1*num2
multiply(4,8)

def divide(num1,num2):
    print(num1/num2)
    return num1/num2
divide(55,5)

def fldiv(num1,num2):
    print(num1//num2)
    return num1//num2
fldiv(45,5)

def remainder(num1,num2):
    print(num1%num2)
    return num1%num2
remainder(87,4)

def sqr(num):
    print(num**2)
    return num**2
sqr(7)

def power(num1,num2):
    print(num1**num2)
    return num1**num2
power(2,5)

def myName(name):
    print(f"Hi {name}")

myName("K_M")