#Palindrome : Palindrome phrase number or a sequence will be same even if it is written backwards 

#program 1
def rev(value):
   reversedd =  value[::-1]
   if reversedd == value:
       print("it is palindrome")
   else:
       print("it is not a palindrome")

result = rev('madam')


#program 2
def rev2(value2):
    temp = value2
    sum = 0
    while value2 > 0:
        r = value2 % 10
        sum = (sum * 10) + r
        value2 = value2 // 10
    if temp == sum:
        print("it is palindrome")
    else:
        print("it is not palindrome")
    return sum

result = rev2(323)
print(result)
