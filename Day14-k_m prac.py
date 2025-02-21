a =[3, 4, 5, 6, 7, 8, 2, -10,11,14,15,18,22]
# count=0
# oddcount=0
# for i in a:
#     if(i%2==0):
#         count+=1
#     else:
#         oddcount+= 1

# print(f"even count is {count} and odd count is {oddcount}")

mini =a[0]
for i in a:
    if(i<mini):
        mini=i
print(mini)

b = [1,2,3,4]
# b.append(5)
# print(b)

# b.clear()
# print(b)

c = b.copy()
print(c)

# b.extend([5,6,7,8,9,10])
# print(b)

b.insert(3,5)
print(b)

b.pop(3)
print(b)

b.remove(4)
print(b)

d = [2,5,4,3,2,6,7,11,13,9]
d.sort()
print(d)
d.reverse()
print(d)

ans= max(d)
print(ans)
ans2= min(d)
print(ans2)