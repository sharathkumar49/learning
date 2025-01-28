

inpStr = '123412345123456'


# O(1) array creation.
freq = [0] * 1000

# O(n) string processing.
for val in [int(inpStr[pos:pos+3]) for pos in range(len(inpStr) - 2)]:
    freq[val] += 1

# O(1) output of relevant array values.
print ([(num, freq[num]) for num in range(1000) if freq[num] > 1])