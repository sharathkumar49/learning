"""
277. Find the Celebrity
https://leetcode.com/problems/find-the-celebrity/

Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.
Implement a function to find the celebrity. If there is no celebrity, return -1.

Constraints:
- 2 <= n <= 100

Example 1:
Input: n = 2, knows = [[1,0]]
Output: 0

Example 2:
Input: n = 3, knows = [[1,0],[2,0],[1,2]]
Output: 0
"""
# The knows API is already defined for you.
# def knows(a: int, b: int) -> bool:

def findCelebrity(n):
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i
    for i in range(n):
        if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
            return -1
    return candidate

# Example usage (requires knows API):
# Not executable as-is without knows() implementation.
