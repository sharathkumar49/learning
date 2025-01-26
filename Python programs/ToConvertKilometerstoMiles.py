kilo = float(input("Enter the kilometers: "))
conv_fac = 0.621371
miles = kilo * conv_fac
print("%0.3f kilometers is equal to  %0.4f" %(kilo, miles))

#Now to convert back them to kilometers
kilometer = miles / conv_fac
print("the kilometer is :",  kilometer)