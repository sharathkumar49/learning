"""
825. Friends Of Appropriate Ages

Given a list of ages, return the number of friend requests made according to the rules:
- A person A will not send a friend request to person B if age[B] <= 0.5 * age[A] + 7, age[B] > age[A], or age[B] > 100 and age[A] < 100.
- Otherwise, A will send a friend request to B.

Example 1:
Input: ages = [16,16]
Output: 2

Example 2:
Input: ages = [16,17,18]
Output: 2

Constraints:
- 1 <= ages.length <= 20000
- 1 <= ages[i] <= 120
"""
def numFriendRequests(ages):
    ages.sort()
    ans = left = 0
    for right, age in enumerate(ages):
        if age < 15:
            continue
        while ages[left] <= 0.5 * age + 7:
            left += 1
        ans += right - left
    count = {}
    for age in ages:
        count[age] = count.get(age, 0) + 1
    for v in count.values():
        ans += v * (v - 1) // 2
    return ans

# Example usage:
print(numFriendRequests([16,16]))  # Output: 2
print(numFriendRequests([16,17,18]))  # Output: 2
