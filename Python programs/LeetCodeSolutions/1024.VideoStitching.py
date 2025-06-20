"""
1024. Video Stitching

You are given a list of video clips and a time T. Return the minimum number of clips needed to cover [0, T]. If not possible, return -1.

Constraints:
- 1 <= clips.length <= 100
- 0 <= clips[i][0] < clips[i][1] <= 100
- 0 <= T <= 100

Example:
Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
Output: 3
Explanation: We take clips [0,2], [1,9], [8,10].
"""
from typing import List

def videoStitching(clips: List[List[int]], T: int) -> int:
    clips.sort()
    res, end, i, n = 0, 0, 0, len(clips)
    while end < T:
        farthest = end
        while i < n and clips[i][0] <= end:
            farthest = max(farthest, clips[i][1])
            i += 1
        if farthest == end:
            return -1
        res += 1
        end = farthest
    return res

# Example usage:
clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
T = 10
print(videoStitching(clips, T))  # Output: 3
