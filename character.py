name = "kundanika234madireddy29"
ans = 0
for i in name:
    if i.isnumeric():
        ans += int(i)
print(ans)

#length of string
name = "Kundanika Madireddy"
count = 0
for i in name:
    count += 1

print(count)

num = 100213402
strNum = str(num)
ans= ""
for i in strNum:
    if i == "0":
        ans += "1"
    else:
        ans+= i
    
print(ans)