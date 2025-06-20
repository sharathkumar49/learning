"""
636. Exclusive Time of Functions
Difficulty: Medium

On a single-threaded CPU, given n functions and a list of logs, each log is a string with function id, start/end, and timestamp. Return the exclusive time of each function.

Example 1:
Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3,4]

Constraints:
1 <= n <= 100
1 <= logs.length <= 500
0 <= function_id < n
0 <= timestamp <= 10^9
"""

def exclusiveTime(n, logs):
    res = [0] * n
    stack = []
    prev = 0
    for log in logs:
        fn, typ, time = log.split(':')
        fn, time = int(fn), int(time)
        if typ == 'start':
            if stack:
                res[stack[-1]] += time - prev
            stack.append(fn)
            prev = time
        else:
            res[stack.pop()] += time - prev + 1
            prev = time + 1
    return res

# Example usage
if __name__ == "__main__":
    print(exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))  # Output: [3,4]
