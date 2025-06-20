"""
1086. High Five

Given a list of scores for students, return the average of each student's top five scores in the format [id, average].

Constraints:
- 1 <= items.length <= 1000
- items[i].length == 2
- 1 <= id, score <= 1000

Example:
Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
"""
from typing import List
from collections import defaultdict

def highFive(items: List[List[int]]) -> List[List[int]]:
    scores = defaultdict(list)
    for id, score in items:
        scores[id].append(score)
    res = []
    for id in sorted(scores):
        top5 = sorted(scores[id], reverse=True)[:5]
        res.append([id, sum(top5)//5])
    return res

# Example usage:
items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
print(highFive(items))  # Output: [[1, 87], [2, 88]]
