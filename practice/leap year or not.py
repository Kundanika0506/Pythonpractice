# year = 2000
# if(year%400==0 or year%4==0 and year%100 !=0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


def is_leap(year):
    leap = False
    if(year%400==0 or year%4==0 and year%100 !=0):
        print(True)
    return leap

print(is_leap(2000))

    
