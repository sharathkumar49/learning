"""
1239. Maximum Length of a Concatenated String with Unique Characters

Given an array of strings arr, return the maximum length of a concatenated string with unique characters.

Constraints:
- 1 <= arr.length <= 16
- 1 <= arr[i].length <= 26
- arr[i] consists of lowercase English letters.

Example:
Input: arr = ["un","iq","ue"]
Output: 4

"""
def maxLength(arr):
    def backtrack(i, curr):
        if len(curr) != len(set(curr)):
            return 0
        if i == len(arr):
            return len(curr)
        return max(backtrack(i+1, curr), backtrack(i+1, curr+arr[i]))
    return backtrack(0, "")

# Example usage
if __name__ == "__main__":
    print(maxLength(["un","iq","ue"]))  # Output: 4
