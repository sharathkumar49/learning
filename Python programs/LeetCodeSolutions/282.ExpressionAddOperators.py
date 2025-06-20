"""
282. Expression Add Operators
https://leetcode.com/problems/expression-add-operators/

Given a string num that contains only digits and an integer target, return all possibilities to add binary operators '+', '-', or '*' between the digits so they evaluate to the target value.

Constraints:
- 1 <= num.length <= 10
- num consists of only digits.
- -2^31 <= target <= 2^31 - 1

Example 1:
Input: num = "123", target = 6
Output: ["1+2+3","1*2*3"]

Example 2:
Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
"""
def addOperators(num, target):
    res = []
    def backtrack(index, path, value, prev):
        if index == len(num):
            if value == target:
                res.append(path)
            return
        for i in range(index+1, len(num)+1):
            tmp = num[index:i]
            if len(tmp) > 1 and tmp[0] == '0':
                break
            n = int(tmp)
            if index == 0:
                backtrack(i, tmp, n, n)
            else:
                backtrack(i, path + '+' + tmp, value + n, n)
                backtrack(i, path + '-' + tmp, value - n, -n)
                backtrack(i, path + '*' + tmp, value - prev + prev * n, prev * n)
    backtrack(0, '', 0, 0)
    return res

# Example usage:
if __name__ == "__main__":
    print(sorted(addOperators("123", 6)))   # Output: ['1+2+3', '1*2*3']
    print(sorted(addOperators("232", 8)))   # Output: ['2*3+2', '2+3*2']
