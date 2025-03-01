arr = [ 43, 34, 55, 23, 27, 12, 14, 18, 3, 5, 2]
max = arr[0]
min = arr[0]
for i in arr:
    if i> max:
        max = i 
    if i < min:
        min = i
print(f"the largest elemnt is {max} and smallest element is {min}")

# another method 
# largest = max(arr)
# smallest = min(arr)
# print(largest,smallest)