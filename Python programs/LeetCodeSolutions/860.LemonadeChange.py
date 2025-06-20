"""
860. Lemonade Change

At a lemonade stand, each lemonade costs $5. Customers pay with $5, $10, or $20 bills. Return true if you can provide change to every customer.

Example 1:
Input: bills = [5,5,5,10,20]
Output: true

Example 2:
Input: bills = [5,5,10,10,20]
Output: false

Constraints:
- 1 <= bills.length <= 10^5
- bills[i] is 5, 10, or 20.
"""
def lemonadeChange(bills):
    five = ten = 0
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True

# Example usage:
print(lemonadeChange([5,5,5,10,20]))  # Output: True
print(lemonadeChange([5,5,10,10,20])) # Output: False
