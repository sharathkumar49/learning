"""
1189. Maximum Number of Balloons

Given a string text, return the maximum number of times the word "balloon" can be formed.

Constraints:
- 1 <= text.length <= 10^4
- text consists of lowercase English letters.

Example:
Input: text = "nlaebolko"
Output: 1

"""
def maxNumberOfBalloons(text):
    from collections import Counter
    count = Counter(text)
    return min(count.get('b',0), count.get('a',0), count.get('l',0)//2, count.get('o',0)//2, count.get('n',0))

# Example usage
if __name__ == "__main__":
    print(maxNumberOfBalloons("nlaebolko"))  # Output: 1
