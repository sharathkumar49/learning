"""
1152. Analyze User Website Visit Pattern

Given three arrays username, timestamp, and website, return the most visited 3-sequence of websites by users. If there is a tie, return the lexicographically smallest sequence.

Constraints:
- 3 <= username.length <= 50
- 1 <= username[i].length <= 10
- 1 <= timestamp[i] <= 10^9
- 1 <= website[i].length <= 10

Example:
Input: username = ["joe","joe","joe","james","james","james","james"], timestamp = [1,2,3,4,5,6,7], website = ["home","about","career","home","cart","maps","home"]
Output: ["home","cart","maps"]

"""
def mostVisitedPattern(username, timestamp, website):
    from collections import defaultdict, Counter
    from itertools import combinations
    data = sorted(zip(timestamp, username, website))
    users = defaultdict(list)
    for t, u, w in data:
        users[u].append(w)
    patterns = Counter()
    for u in users:
        seqs = set(combinations(users[u], 3))
        for seq in seqs:
            patterns[seq] += 1
    return list(min([k for k, v in patterns.items() if v == max(patterns.values())]))

# Example usage
if __name__ == "__main__":
    username = ["joe","joe","joe","james","james","james","james"]
    timestamp = [1,2,3,4,5,6,7]
    website = ["home","about","career","home","cart","maps","home"]
    print(mostVisitedPattern(username, timestamp, website))  # Output: ['home', 'cart', 'maps']
