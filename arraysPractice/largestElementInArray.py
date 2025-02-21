arr = [23, 3, 4, 56, 74, 27, 30, 45, 82]
largest = arr[0]
for i in arr:
    if i > largest:
        largest = i
print(largest)