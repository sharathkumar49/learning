"""
LeetCode 690. Employee Importance

You have a data structure representing a company hierarchy. Each employee has a unique id, an importance value, and a list of direct subordinates' ids.

Given the data of all employees and the id of one employee, return the total importance value of this employee and all their subordinates.

Example 1:
Input: employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], id = 1
Output: 11

Constraints:
- 1 <= employees.length <= 2000
- 1 <= id, importance <= 2000
- 0 <= number of direct subordinates <= 2000
"""
from typing import List

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

def getImportance(employees: List[Employee], id: int) -> int:
    emp_map = {e.id: e for e in employees}
    def dfs(eid):
        emp = emp_map[eid]
        return emp.importance + sum(dfs(subid) for subid in emp.subordinates)
    return dfs(id)

# Example usage
if __name__ == "__main__":
    employees = [Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])]
    print(getImportance(employees, 1))  # Output: 11
