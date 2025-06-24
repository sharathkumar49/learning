"""
LeetCode 1349. Maximum Students Taking Exam

Given a m x n matrix seats, return the maximum number of students that can take the exam without cheating (no two students can sit next to each other horizontally or diagonally).

Constraints:
- 1 <= seats.length <= 8
- 1 <= seats[0].length <= 8
- seats[i][j] is '.' or '#'

Example:
Input: seats = [["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]
Output: 4
"""
def maxStudents(seats):
    m, n = len(seats), len(seats[0])
    dp = [{} for _ in range(m+1)]
    dp[0][0] = 0
    for i in range(1, m+1):
        for prev in dp[i-1]:
            for cur in range(1<<n):
                ok = True
                for j in range(n):
                    if (cur>>j)&1:
                        if seats[i-1][j] == '#' or (j>0 and (cur>>(j-1))&1) or (j>0 and (prev>>(j-1))&1) or (j<n-1 and (prev>>(j+1))&1):
                            ok = False
                            break
                if ok:
                    dp[i][cur] = max(dp[i].get(cur,0), dp[i-1][prev]+bin(cur).count('1'))
    return max(dp[m].values())

# Example usage:
seats = [["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]
print(maxStudents(seats))  # Output: 4
