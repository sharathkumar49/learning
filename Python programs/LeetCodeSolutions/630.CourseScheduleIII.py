"""
630. Course Schedule III
Difficulty: Hard

There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [duration_i, lastDay_i] indicate that the i-th course should be taken continuously for duration_i days and must be finished before or on lastDay_i.
Return the maximum number of courses that can be taken.

Example 1:
Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3

Constraints:
1 <= courses.length <= 10^4
1 <= duration_i, lastDay_i <= 10^4
"""

def scheduleCourse(courses):
    import heapq
    courses.sort(key=lambda x: x[1])
    heap = []
    total = 0
    for duration, lastDay in courses:
        total += duration
        heapq.heappush(heap, -duration)
        if total > lastDay:
            total += heapq.heappop(heap)
    return len(heap)

# Example usage
if __name__ == "__main__":
    print(scheduleCourse([[100,200],[200,1300],[1000,1250],[2000,3200]]))  # Output: 3
