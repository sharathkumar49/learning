"""
842. Split Array into Fibonacci Sequence

Given a string num, split it into a Fibonacci-like sequence. Return any such sequence or [] if it cannot be done.

Example 1:
Input: num = "123456579"
Output: [123,456,579]

Example 2:
Input: num = "11235813"
Output: [1,1,2,3,5,8,13]

Constraints:
- 1 <= num.length <= 200
- num contains only digits.
"""
def splitIntoFibonacci(num):
    n = len(num)
    for i in range(1, min(11, n)):
        for j in range(i+1, min(i+11, n)):
            a, b = num[:i], num[i:j]
            if (a.startswith('0') and a != '0') or (b.startswith('0') and b != '0'):
                continue
            fib = [int(a), int(b)]
            k = j
            while k < n:
                nxt = fib[-1] + fib[-2]
                nxt_s = str(nxt)
                if not num.startswith(nxt_s, k):
                    break
                fib.append(nxt)
                k += len(nxt_s)
            if k == n and len(fib) >= 3:
                return fib
    return []

# Example usage:
print(splitIntoFibonacci("123456579"))  # Output: [123,456,579]
print(splitIntoFibonacci("11235813"))   # Output: [1,1,2,3,5,8,13]
