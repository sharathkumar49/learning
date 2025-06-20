"""
599. Minimum Index Sum of Two Lists
Difficulty: Easy

Given two lists of strings list1 and list2, find the common strings with the least index sum. Return the list of these strings.

Example 1:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]

Example 2:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]

Constraints:
1 <= list1.length, list2.length <= 1000
1 <= list1[i].length, list2[i].length <= 30
list1[i] and list2[i] are strings.
"""

def findRestaurant(list1, list2):
    index1 = {x: i for i, x in enumerate(list1)}
    min_sum = float('inf')
    res = []
    for j, x in enumerate(list2):
        if x in index1:
            s = index1[x] + j
            if s < min_sum:
                min_sum = s
                res = [x]
            elif s == min_sum:
                res.append(x)
    return res

# Example usage
if __name__ == "__main__":
    print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))  # Output: ["Shogun"]
