# name= "Kundanika"
# ans = name[::-1]
# print(ans)

# num = 54
# a = 0
# b = 1
# print(a,b, end=" ")
# for i in range(2,num):
#     c = a +b
#     a = b
#     b = c
#     print(c, end=" ")


name1 = "Dinesh"
ans = name1.lower()[::-1]
if (ans==name1):
    print(f"{name1} is a palindrome ")
else:
    print(f"{name1} is not a palindrome")

a = ["dad", "mom", "level", "kundan", "Uday"]
ans =[]
for i in a:
    if i==i[::-1]:
        ans.append(i)
print(ans)
    
name= ""