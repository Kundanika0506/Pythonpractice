a = [10,20,30,30,40,50,40]
ans =[]
for i in a:
    if(i not in ans):
        ans.append(i)
    else:
        print(i)

print(len(ans))

# print(len(list(set(a))))

a= [2,3,4,1,5,8,13,12,14,16,21,24]
count =0
oddcount=0
for i in a:
    if(i%2==0):
        count+=1
    else:
        oddcount+=1

ans =[]
# ans =[x for x in a if(x%2==0)]
for i in a:
    if(i%2==0):
        ans.append(i)
print(ans)
