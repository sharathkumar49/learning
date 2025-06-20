"""
651. 4 Keys Keyboard
Difficulty: Medium

Imagine you have a special keyboard with the following keys:
- A: Print one 'A' on the screen.
- Ctrl-A: Select all the text.
- Ctrl-C: Copy all the selected text.
- Ctrl-V: Paste the copied text.
You can press each key any number of times. Given an integer N, return the maximum number of 'A's you can print on the screen with N keystrokes.

Example 1:
Input: N = 3
Output: 3

Example 2:
Input: N = 7
Output: 9

Constraints:
1 <= N <= 50
"""

def maxA(N):
    dp = [0] * (N+1)
    for i in range(1, N+1):
        dp[i] = dp[i-1] + 1
        for j in range(2, i-2+1):
            dp[i] = max(dp[i], dp[j-2]*(i-j+1))
    return dp[N]

# Example usage
if __name__ == "__main__":
    print(maxA(3))  # Output: 3
    print(maxA(7))  # Output: 9
