listvalues = list(input("Enter the values: ").split())
print("The entered values are", listvalues)
mx = max(listvalues[0], listvalues[1])
secondmax = min(listvalues[0], listvalues[1])
n = len(listvalues)
for i in range(2,n):
    if listvalues[i] > mx:
        secondmax = mx 
        mx = listvalues[i]
    elif listvalues[i] > secondmax and listvalues[i] != mx :
        secondmax = listvalues[i]
print("The second max value is", secondmax)



#To find largest among three number:
values = list(input("Enter three values:").split())
mx = max(values)
print("The largest value is", mx)


#without using function
if(values[0]>=values[1] and values[0]>=values[2]):
    print("The largest value is:", values[0])
elif(values[1]>=values[0] and values[1]>=values[2]):
    print("The largest value is:", values[1])
else:
    print("The largest value is:", values[2])