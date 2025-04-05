
#Python | Sort Python Dictionaries by Key or Value


#Displaying the Keys Alphabetically:
def dicti():
    batman = {"batman" : "bruce", "catwoman": "selina", "joker": "heath ledger"}
    for i in sorted(batman.keys()):
        print(i, end=' ')

dicti()




#Sorting the Keys and Values in Alphabetical Order using the Key.
print("\nSorting the Keys and Values in Alphabetical Order using the Key.")
def dictii():
    batman = {"batman" : "bruce", "catwoman": "selina", "joker": "heath ledger"}
    for i in sorted(batman.keys()):
        print(i, batman[i], end=" ")

dictii()




#Sorting the Keys and Values in Alphabetical Order using the Value.
print("\nSorting the Keys and Values in Alphabetical Order using the value.")
def dictiv():
    batman = {"batman" : "bruce", "catwoman": "selina", "joker": "heath ledger"}
    print(sorted(batman.items(), key = lambda kv : (kv[1], kv[0])))

dictiv()




#Using sorted dictionary
from collections import OrderedDict
def dictis():
    batman = {"batman" : "bruce", "catwoman": "selina", "joker": "heath ledger"}
    batman2 = OrderedDict(sorted(batman.items()))
    print(batman2)


'''
Learning Outcome: 
 
How to handle a dictionary.
Dictionary has O(1) search time complexity whereas List has O(n) time complexity. So it is recommended to 
use the dictionary where ever possible.
The best application of dictionary can be seen in Twitter Sentiment Analysis where analysis Twitter sentiments are 
analysed, using Lexicon approach.
'''


