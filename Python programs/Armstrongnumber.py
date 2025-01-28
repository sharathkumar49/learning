# Armstrong number is such that the sum of the cube of all of its digits is equal to same number
# 153 = 1**3 + 5**3 + 3**3 = 153


num = int(input("enter the number: ")) 
temp = num 
sum = 0

# 153
while num > 0:
    r = num % 10 # r = 5
    sum += r**3  # sum = 152
    num = num // 10  # num = 0


print(sum)



if temp == sum:
    print("it is an armstrong number")
else:
    print("it's not an armstrong number ")
