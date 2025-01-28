

count = 0
value = input("Enter the string:")
cha = input("Enter the character:")
for i in value:
    if cha == i:
        count+= 1

print(count)


my_string = "Programiz"
my_char = "r"

print(my_string.count(my_char))