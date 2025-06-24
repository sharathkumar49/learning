"""
1196. How Many Apples Can You Put into the Basket

Given an array weight of apples, return the maximum number of apples you can put in a basket with a weight limit of 5000.

Constraints:
- 1 <= weight.length <= 10^5
- 1 <= weight[i] <= 10000

Example:
Input: weight = [100,200,150,1000]
Output: 4

"""
def maxNumberOfApples(weight):
    weight.sort()
    total = 0
    count = 0
    for w in weight:
        if total + w > 5000:
            break
        total += w
        count += 1
    return count

# Example usage
if __name__ == "__main__":
    print(maxNumberOfApples([100,200,150,1000]))  # Output: 4
