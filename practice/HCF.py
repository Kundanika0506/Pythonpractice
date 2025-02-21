num1 = 36
num2 = 48
ans = 1
for i in range(2,min(num1,num2)+1):
    if(num1%i==0 and num2%i==0):
        ans = i
print(ans)


num = 11
a,b = 0,1
print(a,b,end=" ")
for i in range(2,num):
    c = a+b
    a =b
    b = c
    print(c,end=" ")