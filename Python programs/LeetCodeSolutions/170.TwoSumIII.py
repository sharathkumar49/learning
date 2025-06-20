"""
170. Two Sum III - Data structure design
https://leetcode.com/problems/two-sum-iii-data-structure-design/

Design a data structure that accepts a stream of integers and checks if it has a pair of numbers that sum up to a particular value.

Constraints:
- -10^5 <= number <= 10^5
- At most 5 * 10^4 calls will be made to add and find.

Example:
Input: ["TwoSum","add","add","find"], [[],[1],[3],[4]]
Output: [null,null,null,true]
"""
class TwoSum:
    def __init__(self):
        self.counts = {}
    def add(self, number: int) -> None:
        self.counts[number] = self.counts.get(number, 0) + 1
    def find(self, value: int) -> bool:
        for num in self.counts:
            complement = value - num
            if complement == num:
                if self.counts[num] > 1:
                    return True
            elif complement in self.counts:
                return True
        return False

# Example usage:
if __name__ == "__main__":
    ts = TwoSum()
    ts.add(1)
    ts.add(3)
    ts.add(5)
    print(ts.find(4))  # Output: True
    print(ts.find(7))  # Output: False
