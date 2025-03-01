a = [1, 3, 2,  4, 5 , 8, 7, 6, 10, 9]
firsthalf= a[:len(a)//2]
firsthalf.sort()

secondhalf= a[len(a)//2:]
secondhalf.sort()
secondhalf.reverse()
print(firsthalf)
print(secondhalf)
print(firsthalf+secondhalf)
