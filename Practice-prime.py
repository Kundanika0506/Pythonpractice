def isPrime(num):
    count = 0
    for i in range(1,num+1):
        if(num%i==0):
            count +=1
    if(count==2):
        print(f"{num} is a prime number")

for i in range(1,1001):
    isPrime(i)

num = 48
for i in range(1,21):
    print(f"{num} X {i} is {num*i}")