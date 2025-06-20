"""
LeetCode 692. Top K Frequent Words

Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

Example 1:
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]

Example 2:
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]

Constraints:
- 1 <= words.length <= 500
- 1 <= words[i] <= 10
- words[i] consists of lowercase English letters.
- k is in the range [1, The number of unique words]
"""
from typing import List
from collections import Counter

def topKFrequent(words: List[str], k: int) -> List[str]:
    count = Counter(words)
    return sorted(count, key=lambda x: (-count[x], x))[:k]

# Example usage
if __name__ == "__main__":
    print(topKFrequent(["i","love","leetcode","i","love","coding"], 2))  # Output: ['i', 'love']
    print(topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))  # Output: ['the', 'is', 'sunny', 'day']
