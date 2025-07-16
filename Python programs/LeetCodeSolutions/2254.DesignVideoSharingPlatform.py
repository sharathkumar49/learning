"""
LeetCode 2254. Design Video Sharing Platform

Design a video sharing platform with upload, remove, and view operations.

Example:
Input: ["VideoSharingPlatform","upload","remove","view"], [[],["video1"],[0],[0]]
Output: [null,0,null,1]

Constraints:
- 1 <= operations.length <= 10^5
"""

class VideoSharingPlatform:
    def __init__(self):
        self.videos = {}
        self.next_id = 0
    def upload(self, video):
        self.videos[self.next_id] = [video, 0]
        self.next_id += 1
        return self.next_id - 1
    def remove(self, videoId):
        if videoId in self.videos:
            del self.videos[videoId]
    def view(self, videoId):
        if videoId in self.videos:
            self.videos[videoId][1] += 1
            return self.videos[videoId][1]
        return -1

# Example usage:
# vsp = VideoSharingPlatform()
# id1 = vsp.upload("video1")
# vsp.remove(id1)
# print(vsp.view(id1))  # Output: -1
