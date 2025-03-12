num = 1202010

ans =""
for i in str(num):
    if i != "0":
        ans+=i
    else:
        ans+="1"
print(int(ans))

# strNum = str(num)
# print(strNum.replace("0","1"))