"""
LeetCode 2286. Booking Concert Tickets in Groups

Design a system to book concert tickets in groups.

Example:
Input: ["BookMyShow","gather","scatter"], [[],[5,2],[5,6]]
Output: [null,[0,0],true]

Constraints:
- 1 <= operations.length <= 10^5
"""

class BookMyShow:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.seats = [[0]*m for _ in range(n)]
    def gather(self, k, maxRow):
        for i in range(maxRow+1):
            cnt = 0
            for j in range(self.m):
                if self.seats[i][j] == 0:
                    cnt += 1
                else:
                    cnt = 0
                if cnt == k:
                    for x in range(j-k+1, j+1):
                        self.seats[i][x] = 1
                    return [i, j-k+1]
        return []
    def scatter(self, k, maxRow):
        cnt = 0
        for i in range(maxRow+1):
            for j in range(self.m):
                if self.seats[i][j] == 0:
                    cnt += 1
        if cnt < k:
            return False
        for i in range(maxRow+1):
            for j in range(self.m):
                if self.seats[i][j] == 0 and k > 0:
                    self.seats[i][j] = 1
                    k -= 1
        return True

# Example usage:
# bms = BookMyShow(5, 10)
# print(bms.gather(2, 2))
# print(bms.scatter(6, 4))
