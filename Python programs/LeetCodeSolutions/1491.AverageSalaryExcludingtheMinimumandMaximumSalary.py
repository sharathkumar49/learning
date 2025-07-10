"""
LeetCode 1491. Average Salary Excluding the Minimum and Maximum Salary

Given an array salary where salary[i] is the salary of the employee, return the average salary excluding the minimum and maximum salary.

Constraints:
- 3 <= salary.length <= 100
- 1000 <= salary[i] <= 10^6

Example:
Input: salary = [4000,3000,1000,2000]
Output: 2500.0
"""
def average(salary):
    salary.sort()
    return sum(salary[1:-1]) / (len(salary) - 2)

# Example usage:
salary = [4000,3000,1000,2000]
print(average(salary))  # Output: 2500.0
