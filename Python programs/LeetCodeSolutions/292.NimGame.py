"""
292. Nim Game
https://leetcode.com/problems/nim-game/

You are playing the following Nim Game with your friend:
- Initially, there is a heap of stones on the table.
- You and your friend will alternate taking turns, and you go first.
- On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
- The one who removes the last stone is the winner.
Given n, the number of stones in the heap, return true if you can win the game assuming both players play optimally, otherwise return false.

Constraints:
- 1 <= n <= 2^31 - 1

Example 1:
Input: n = 4
Output: false

Example 2:
Input: n = 1
Output: true

Example 3:
Input: n = 2
Output: true
"""
def canWinNim(n):
    return n % 4 != 0

# Example usage:
if __name__ == "__main__":
    print(canWinNim(4))  # Output: False
    print(canWinNim(1))  # Output: True
    print(canWinNim(2))  # Output: True
