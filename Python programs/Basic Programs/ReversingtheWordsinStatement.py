


mystring = "If you work for a living, why do you kill yourself working?"
mylst = mystring.split()
print(mylst)
finalword = ''
for i in mylst[::-1]:
    finalword = finalword + i + " "
print(finalword)
