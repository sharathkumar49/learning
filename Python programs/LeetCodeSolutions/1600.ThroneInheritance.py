"""
LeetCode 1600. Throne Inheritance

Design a ThroneInheritance class to simulate the inheritance of a king's throne. Implement the following methods:
- ThroneInheritance(string kingName): Initializes the class with the name of the king.
- void birth(string parentName, string childName): Indicates that parentName has a new child childName.
- void death(string name): Indicates the death of name.
- List<string> getInheritanceOrder(): Returns the current inheritance order.

Example:
Input: ["ThroneInheritance","birth","birth","birth","birth","birth","death","getInheritanceOrder"], [["king"],["king","andy"],["king","bob"],["king","catherine"],["andy","matthew"],["bob","alex"],["bob"],[]]
Output: [null,null,null,null,null,null,null,["king","andy","matthew","catherine","alex"]]

Constraints:
- 1 <= kingName.length, parentName.length, childName.length <= 15
- kingName, parentName, childName are lowercase English letters.
- At most 10^5 calls will be made to birth, death, and getInheritanceOrder.
"""

class ThroneInheritance:
    def __init__(self, kingName):
        self.king = kingName
        self.family = {kingName: []}
        self.dead = set()
    def birth(self, parentName, childName):
        if parentName not in self.family:
            self.family[parentName] = []
        self.family[parentName].append(childName)
        self.family[childName] = []
    def death(self, name):
        self.dead.add(name)
    def getInheritanceOrder(self):
        res = []
        def dfs(name):
            if name not in self.dead:
                res.append(name)
            for child in self.family[name]:
                dfs(child)
        dfs(self.king)
        return res

# Example usage:
# t = ThroneInheritance("king")
# t.birth("king", "andy")
# t.birth("king", "bob")
# t.birth("king", "catherine")
# t.birth("andy", "matthew")
# t.birth("bob", "alex")
# t.death("bob")
# print(t.getInheritanceOrder())  # Output: ['king', 'andy', 'matthew', 'catherine', 'alex']
