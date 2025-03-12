thisdict = {
    "brand" : "ford",
    "model" : "Mustang",
    "year" : 1964,
    "colour": ["red", "black", "blue", "white"]
}
print(thisdict)
print(thisdict["brand"])

print(thisdict.get("model"))

print(len(thisdict))

thisdict= dict(name= "kundan", age= 18 , hobbies= "dancing")
print(thisdict.keys())
print(thisdict.items())
print(thisdict.values())

thisdict.update(school="UW")
print(thisdict)
print(thisdict.popitem())
print(thisdict)

my_data = {
    "name":"Kundanika",
    "age" : 18,
    "Graduated":False,
    "key":"value"
}

print(type(my_data))
my_data["age"] = 20
my_second = my_data.copy()
# print(my_second)
print(my_data.get("name","NA"))
print(my_data.items())
print(my_data.keys())
print(my_data.values())

rest_info = {
    "lastName" : "Madireddy",
    "middleName":""
}
my_data.update(rest_info)
print(my_data)
print(my_data.pop("Graduated"))

my_data.popitem()
print(my_data)


# arr = "kundanika"
# ans ={}
# for i in arr:
#     if i not in ans.keys():
#         ans[i] = 1
#     else:
#         ans[i] = ans.get(i)+1
# print(ans)



# name = "Kundanika madireddy"
# ans = ""
# for i in name:
#     if i != " ":
#         ans+=i
# print(ans)
