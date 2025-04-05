value = "hello"
valuelength = len(value)
print("The lenth of the string is: ", valuelength)
for i in range(valuelength-1, -1, -1):
    print(value[i])
    

#workflow of above program
x = range(6, -1, -1)
for n in x:
  print(n)

#Output: 6 5 4 3 2 1 0



#second method
newvalue = value[::-1]
print(newvalue)