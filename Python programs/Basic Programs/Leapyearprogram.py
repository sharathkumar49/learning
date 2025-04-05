# for understanding leap year concept, visit pycharm and under the section hackerrank
# and also refer this source: 
#  https://www.almanac.com/content/when-next-leap-year#:~:text=A%20year%20may%20be%20a,years%201600%20and%202000%20were.)


def is_leap(year = 1700):
    if year % 4 == 0:
        leap = True
        if(year % 100 == 0):
            if(year % 400 == 0 and year % 100 == 0):
                leap = True
            else:
                leap = False
    else:
        leap = False
    return leap


#driver code
year = int(input("Enter the year: "))
finalvalue = is_leap(year)
if (finalvalue == True):
    print("it is a leap year")
else:
    print("it's not a leap year")
