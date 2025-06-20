"""
444. Sequence Reconstruction

Check whether the original sequence can be uniquely reconstructed from the sequences in seqs. The original sequence is a permutation of the integers from 1 to n, with 1 <= n <= 10^4. Reconstruct the sequence by reading the sequences in seqs and return true if it can be uniquely reconstructed.

Constraints:
- 1 <= n <= 10^4
- The length of org is between 1 and 10^4
- 1 <= seqs[i].length <= 10^4
- seqs[i][j] is in the range [1, n]

Example:
Input: org = [1,2,3], seqs = [[1,2],[1,3]]
Output: False
"""

from collections import defaultdict, deque

class Solution:
    def sequenceReconstruction(self, org: list, seqs: list) -> bool:
        graph = defaultdict(set)
        indegree = defaultdict(int)
        nodes = set()
        for seq in seqs:
            for i in range(len(seq)):
                nodes.add(seq[i])
                if i > 0 and seq[i] not in graph[seq[i-1]]:
                    graph[seq[i-1]].add(seq[i])
                    indegree[seq[i]] += 1
        if nodes != set(org):
            return False
        queue = deque([x for x in org if indegree[x] == 0])
        idx = 0
        while queue:
            if len(queue) > 1:
                return False
            curr = queue.popleft()
            if org[idx] != curr:
                return False
            idx += 1
            for nei in graph[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return idx == len(org)

# Example usage:
sol = Solution()
print(sol.sequenceReconstruction([1,2,3], [[1,2],[1,3]]))  # Output: False
