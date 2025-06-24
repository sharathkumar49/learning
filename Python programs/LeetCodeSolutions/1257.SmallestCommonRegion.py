"""
1257. Smallest Common Region

Given a list of regions and two region names, return their smallest common region.

Constraints:
- 2 <= regions.length <= 10^4
- 2 <= regions[i].length <= 20
- 1 <= regions[i][j].length, region1.length, region2.length <= 20

Example:
Input: regions = [["Earth","North America","South America"],["North America","United States","Canada"],["United States","New York","Boston"],["Canada","Ontario","Quebec"],["South America","Brazil"]], region1 = "Quebec", region2 = "New York"
Output: "North America"

"""
def findSmallestRegion(regions, region1, region2):
    parent = {}
    for region in regions:
        for child in region[1:]:
            parent[child] = region[0]
    ancestors = set()
    while region1:
        ancestors.add(region1)
        region1 = parent.get(region1)
    while region2 not in ancestors:
        region2 = parent.get(region2)
    return region2

# Example usage
if __name__ == "__main__":
    regions = [["Earth","North America","South America"],["North America","United States","Canada"],["United States","New York","Boston"],["Canada","Ontario","Quebec"],["South America","Brazil"]]
    print(findSmallestRegion(regions, "Quebec", "New York"))  # Output: "North America"
