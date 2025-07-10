"""
LeetCode 1792. Maximum Average Pass Ratio

Given a list of classes with students passed and total students, and extra students, maximize the average pass ratio after assigning the extra students.

Example 1:
Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
Output: 1.0

Constraints:
- 1 <= classes.length <= 10^5
- 1 <= passedi <= totali <= 10^5
- 1 <= extraStudents <= 10^5
"""

def maxAverageRatio(classes, extraStudents):
    import heapq
    heap = []
    for p, t in classes:
        heapq.heappush(heap, (-(p+1)/(t+1) + p/t, p, t))
    for _ in range(extraStudents):
        diff, p, t = heapq.heappop(heap)
        p += 1
        t += 1
        heapq.heappush(heap, (-(p+1)/(t+1) + p/t, p, t))
    return sum(p/t for _, p, t in heap) / len(classes)

# Example usage:
# classes = [[1,2],[3,5],[2,2]]
# extraStudents = 2
# print(maxAverageRatio(classes, extraStudents))  # Output: 1.0
