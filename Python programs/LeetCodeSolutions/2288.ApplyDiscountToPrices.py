"""
LeetCode 2288. Apply Discount to Prices

Given sentence and discount, return the sentence with discounted prices.

Example:
Input: sentence = "The price is $100 and $200.", discount = 20
Output: "The price is $80.00 and $160.00."

Constraints:
- 1 <= sentence.length <= 1000
- 1 <= discount <= 100
"""

def discountPrices(sentence, discount):
    import re
    def apply(m):
        price = float(m.group(1))
        price = price * (100-discount)/100
        return "$%.2f" % price
    return re.sub(r'\$(\d+)', apply, sentence)

# Example usage:
# print(discountPrices("The price is $100 and $200.", 20))  # Output: "The price is $80.00 and $160.00."
