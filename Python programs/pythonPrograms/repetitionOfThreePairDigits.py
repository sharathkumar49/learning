

# Question: Given a string of a million numbers (Pi for example),
# write a function/program that returns all repeating 3 digit numbers
# and number of repetition greater than 1

# For example: if the string was: 123412345123456 then the function/program would return:
#
# 123 - 3 times
# 234 - 3 times
# 345 - 2 times





## Method 1:

inpStr = '123412345123456'

# O(1) array creation.
freq = [0] * 1000

# O(n) string processing.
for val in [int(inpStr[pos:pos+3]) for pos in range(len(inpStr) - 2)]:
    freq[val] += 1

# O(1) output of relevant array values.
print ([(num, freq[num]) for num in range(1000) if freq[num] > 1])


## Method 2:
inpStr = '123412345123456'
freq = {}

for val in [int(inpStr[pos:pos+3]) for pos in range(len(inpStr) - 2)]:
    if val in freq:
        freq[val] += 1
    else:
        freq.update({val : 1})

print([(k, v) for k, v in freq.items() if freq[k] > 1])
