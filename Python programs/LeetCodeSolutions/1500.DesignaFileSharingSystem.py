"""
LeetCode 1500. Design a File Sharing System

Design a file sharing system with the following methods:
- join(ownedChunks): Returns the user ID of the new user.
- leave(userID): Removes the user from the system.
- request(userID, chunkID): Returns a list of user IDs who have the chunk, and adds the chunk to the user's ownedChunks.

Constraints:
- 1 <= chunkCount <= 10^4
- 1 <= ownedChunks.length <= chunkCount
- 1 <= chunkID <= chunkCount
- At most 10^4 calls will be made to join, leave, and request.

Example:
Input: ["FileSharing","join","join","join","request","request","leave","request"], [[4],[[],[2,3]],[[],[1,2]],[[],[1,3]],[1,2],[2,3],[1],[3,1]]
Output: [null,1,2,3,[2,3],[1,3],null,[3]]
"""
class FileSharing:
    def __init__(self, m):
        self.chunks = {}
        self.users = {}
        self.next_id = 1
    def join(self, ownedChunks):
        uid = self.next_id
        self.next_id += 1
        self.users[uid] = set(ownedChunks)
        for c in ownedChunks:
            self.chunks.setdefault(c, set()).add(uid)
        return uid
    def leave(self, userID):
        if userID in self.users:
            for c in self.users[userID]:
                self.chunks[c].remove(userID)
                if not self.chunks[c]:
                    del self.chunks[c]
            del self.users[userID]
    def request(self, userID, chunkID):
        res = sorted(self.chunks.get(chunkID, []))
        if userID in self.users:
            self.users[userID].add(chunkID)
            self.chunks.setdefault(chunkID, set()).add(userID)
        return res

# Example usage:
# fs = FileSharing(4)
# id1 = fs.join([2,3])
# id2 = fs.join([1,2])
# id3 = fs.join([1,3])
# print(fs.request(1,2))  # Output: [2,3]
