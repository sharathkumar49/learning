


userword = input("Enter the word: ")
userword = userword.casefold()
charfreq ={}

for char in userword:
    if char in charfreq:
        charfreq[char] += 1
    else:
        charfreq[char] = 1 #  charfreq.update({'char': 1})
        


print(charfreq)
charfreqsorted = sorted(charfreq.items(), key = lambda kv : kv[1], reverse=True)
print(charfreqsorted[0])
