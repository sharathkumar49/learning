"""
LeetCode 1912. Design Movie Rental System

Design a system to support searching, renting, and returning movies from shops.

Example:
Input: MovieRentalSystem(3, [[0,1,5],[0,2,6],[1,2,4],[2,1,2]]), search(1), rent(0,1), drop(0,1), report()
Output: [[0,1],[1,2],[2,1],[0,2],[1,2]]

Constraints:
- 1 <= n, entries.length <= 10^5
- 1 <= shop, movie, price <= 10^5
"""

import heapq
from collections import defaultdict

class MovieRentalSystem:
    def __init__(self, n, entries):
        self.price = defaultdict(dict)
        self.available = defaultdict(list)
        self.rented = []
        for shop, movie, price in entries:
            self.price[movie][shop] = price
            heapq.heappush(self.available[movie], (price, shop))
    def search(self, movie):
        res = []
        avail = self.available[movie][:]
        seen = set()
        while avail and len(res) < 5:
            price, shop = heapq.heappop(avail)
            if shop not in seen:
                res.append([shop, price])
                seen.add(shop)
        return res
    def rent(self, shop, movie):
        price = self.price[movie][shop]
        self.available[movie].remove((price, shop))
        heapq.heapify(self.available[movie])
        heapq.heappush(self.rented, (price, shop, movie))
    def drop(self, shop, movie):
        price = self.price[movie][shop]
        self.rented.remove((price, shop, movie))
        heapq.heapify(self.rented)
        heapq.heappush(self.available[movie], (price, shop))
    def report(self):
        res = []
        rented = self.rented[:]
        heapq.heapify(rented)
        while rented and len(res) < 5:
            price, shop, movie = heapq.heappop(rented)
            res.append([shop, movie])
        return res

# Example usage:
# mrs = MovieRentalSystem(3, [[0,1,5],[0,2,6],[1,2,4],[2,1,2]])
# print(mrs.search(1))
