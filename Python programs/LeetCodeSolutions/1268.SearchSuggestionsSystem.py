"""
LeetCode 1268. Search Suggestions System

You are given an array of strings products and a string searchWord. Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have a common prefix as searchWord up to that character and be lexicographically minimum.

Constraints:
- 1 <= products.length <= 1000
- 1 <= products[i].length <= 3000
- 1 <= searchWord.length <= 1000
- All products[i] and searchWord consist of lowercase English letters.

Example:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
"""
def suggestedProducts(products, searchWord):
    products.sort()
    res, prefix = [], ''
    for c in searchWord:
        prefix += c
        matches = [p for p in products if p.startswith(prefix)]
        res.append(matches[:3])
    return res

# Example usage:
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
print(suggestedProducts(products, searchWord))
# Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
