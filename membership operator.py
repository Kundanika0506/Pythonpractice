name = "Mainstream agency"    
for i in name:
    print(i)

name2 = "Baden coffee"
count = 0
for i in name2:
    count += 1
print(count)

charact = "g"
vowels = "aeiou"
if(charact in vowels):
    print("vowel")
else:
    print("consonant")

name3 = "Madireddy"
vowels = "aeiouAEIOU"
count = 0
for i in name3:
    if i in vowels:
        count += 1
print(count)

name4 = "Windows"
ans = ""
for i in name4:
    if i not in "aeiouAEIOU":
        ans += i
print(ans)