a =[2,3,4,5,6,7,8,10,11,1,12,16,20,24]
maxi = a[0]
mini=a[0]
for i in a:
    if(i>maxi):
        maxi=i
    if(i<mini):
        mini=i


print(f"{maxi} is the greatest number and {mini} is the smallest number")
   
# mini = a[0]
# mini2= a[0]
# for i in a:
#     if(i<mini):
#         mini=i
# for i in a:
#     if(i<mini2):
#         if(i!=mini):
#             mini2=i
# print(mini2)

sum = 0
for i in a:
    sum+=i
print(sum)

# ans=a[::-1]
# print(ans)

# a.reverse()
# print(a)

# ans =[]
# for i in range(len(a)-1,-1,-1):
#     ans.append(a[i])
# print(ans)

firsthalf= a[:len(a)//2]
firsthalf.sort()

secondhalf= a[len(a)//2:]
secondhalf.sort()
secondhalf.reverse()
print(firsthalf+secondhalf)

# firsthalf= a[:len(a)//2]
# firsthalf.sort()

# secondhalf= a[len(a)//2:]
# secondhalf.sort(reverse=True)

# print(firsthalf+secondhalf)
