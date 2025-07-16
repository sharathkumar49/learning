"""
LeetCode 2227. Encrypt and Decrypt Strings

Implement an encryption and decryption system for strings.

Example:
Input: keys = ["a","b","c"], values = ["aa","bb","cc"], dictionary = ["abc","acb"]
Output: 2

Constraints:
- 1 <= keys.length == values.length <= 26
- 1 <= dictionary.length <= 100
"""

class Encrypter:
    def __init__(self, keys, values, dictionary):
        self.enc = {k:v for k,v in zip(keys, values)}
        self.dec = {v:k for k,v in zip(keys, values)}
        self.dict = set(dictionary)
    def encrypt(self, word):
        return ''.join(self.enc.get(c, '') for c in word)
    def decrypt(self, word):
        def dfs(i, path):
            if i == len(word):
                return path in self.dict
            for k in self.dec:
                if word.startswith(k, i):
                    if dfs(i+len(k), path+self.dec[k]):
                        return True
            return False
        return sum(dfs(0, w) for w in self.dict)

# Example usage:
# e = Encrypter(["a","b","c"],["aa","bb","cc"],["abc","acb"])
# print(e.encrypt("abc"))
