"""
LeetCode 1700. Number of Students Unable to Eat Lunch

The school cafeteria offers lunch to n students. Each student prefers either a square or a circular sandwich. The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step, if the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue. Otherwise, they will go to the end of the queue. This continues until none of the students want the sandwich on the top of the stack.

Return the number of students that are unable to eat.

Example 1:
Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0

Constraints:
- 1 <= students.length, sandwiches.length <= 100
- students[i] is 0 or 1.
- sandwiches[i] is 0 or 1.
"""

def countStudents(students, sandwiches):
    from collections import deque
    students = deque(students)
    sandwiches = deque(sandwiches)
    count = 0
    while students and count < len(students):
        if students[0] == sandwiches[0]:
            students.popleft()
            sandwiches.popleft()
            count = 0
        else:
            students.append(students.popleft())
            count += 1
    return len(students)

# Example usage:
# students = [1,1,0,0]
# sandwiches = [0,1,0,1]
# print(countStudents(students, sandwiches))  # Output: 0
