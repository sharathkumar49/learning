"""
332. Reconstruct Itinerary

You are given a list of airline tickets represented by pairs of departure and arrival airports [from, to]. Reconstruct the itinerary in order and return it. All of the tickets belong to a man who departs from 'JFK'. If there are multiple valid itineraries, return the itinerary that has the smallest lexical order when read as a single string.

Constraints:
- 1 <= tickets.length <= 300
- tickets[i].length == 2
- from[i] != to[i]
- All the tickets form at least one valid itinerary.
"""
from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        route = []
        def visit(airport):
            while graph[airport]:
                visit(graph[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]

# Example usage:
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print(Solution().findItinerary(tickets))  # Output: ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']
