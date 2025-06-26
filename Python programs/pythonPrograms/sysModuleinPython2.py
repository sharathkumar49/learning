
import sys
n = len(sys.argv)
print("the n value", n)
sum = 0
for i in range(1, n):
    sum += int(sys.argv[i])
print(sum)
