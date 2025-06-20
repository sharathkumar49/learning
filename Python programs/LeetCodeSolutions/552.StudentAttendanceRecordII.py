#  552. Student Attendance Record II
#  Difficulty: Hard
# 
#  An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:
# 
#  'A': Absent.
#  'L': Late.
#  'P': Present.
# 
#  A student is eligible for an attendance award if they meet both of the following criteria:
#  1. The student was absent ('A') for strictly fewer than 2 days total.
#  2. The student was never late ('L') for 3 or more consecutive days.
# 
#  Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 10^9 + 7.
# 
#  Example 1:
#  Input: n = 2
#  Output: 8
#  Explanation: There are 8 records with length 2 that are eligible for an award:
#  "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
#  Only "AA" is not eligible because there are 2 absences.
# 
#  Constraints:
#  1 <= n <= 100000

MOD = 10**9 + 7

def checkRecord(n: int) -> int:
    # dp[i][a][l]: number of ways for length i, a absents, l consecutive lates
    dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(1, n+1):
        for a in range(2):
            for l in range(3):
                # Add 'P'
                dp[i][a][0] = (dp[i][a][0] + dp[i-1][a][l]) % MOD
                # Add 'A'
                if a > 0:
                    dp[i][a][0] = (dp[i][a][0] + dp[i-1][a-1][l]) % MOD
                # Add 'L'
                if l > 0:
                    dp[i][a][l] = (dp[i][a][l] + dp[i-1][a][l-1]) % MOD
    return sum(dp[n][a][l] for a in range(2) for l in range(3)) % MOD

# Example usage
if __name__ == "__main__":
    print(checkRecord(2))  # Output: 8
