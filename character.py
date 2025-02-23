# name = "kundanika234madireddy29"
# ans = 0
# for i in name:
#     if i.isnumeric():
#         ans += int(i)
# print(ans)

# #length of string
# name = "Kundanika Madireddy"
# count = 0
# for i in name:
#     count += 1

# print(count)

# num = 100213402
# strNum = str(num)
# ans= ""
# for i in strNum:
#     if i == "0":
#         ans += "1"
#     else:
#         ans+= i
    
# print(ans)


# arr = [12, 3, 5, 7, 10]
# sum = 0 
# for i in arr:
#     sum += i
# print(sum)

arr = [12, 3, 5, 7, 10]
ans = []
for i in arr:
    if(i>5):
        ans.append(i)
print(ans)

def greaterthan5(n):
    if n >5:
        return True
ans = list(filter(greaterthan5, arr))
print(ans)

lst = list(filter(lambda x : x>5 , arr))
print(lst)