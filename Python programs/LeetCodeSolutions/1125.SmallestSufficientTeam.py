"""
1125. Smallest Sufficient Team

Given a list of required skills and a list of people with various skills, return the smallest sufficient team of people such that all required skills are covered.

Constraints:
- 1 <= req_skills.length <= 16
- 1 <= people.length <= 60
- 1 <= people[i].length <= 16
- req_skills and people[i] consist of lowercase English letters.

Example:
Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]
"""
from typing import List

def smallestSufficientTeam(req_skills: List[str], people: List[List[str]]) -> List[int]:
    skill_index = {skill: i for i, skill in enumerate(req_skills)}
    n = len(people)
    dp = {0: []}
    for i, skills in enumerate(people):
        his_skill = 0
        for skill in skills:
            if skill in skill_index:
                his_skill |= 1 << skill_index[skill]
        for comb, team in list(dp.items()):
            new_comb = comb | his_skill
            if new_comb not in dp or len(dp[new_comb]) > len(team) + 1:
                dp[new_comb] = team + [i]
    return dp[(1 << len(req_skills)) - 1]

# Example usage:
req_skills = ["java","nodejs","reactjs"]
people = [["java"],["nodejs"],["nodejs","reactjs"]]
print(smallestSufficientTeam(req_skills, people))  # Output: [0, 2]
