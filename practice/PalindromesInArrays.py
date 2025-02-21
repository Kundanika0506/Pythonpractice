a = ["level","kundan","dad","mom","malayalam"]
ans =""
for i in a:
    if(i==i[::-1]):
        if(len(i)>len(ans)):
            ans=i
print(ans)    

