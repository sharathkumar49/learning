"""
271. Encode and Decode Strings
https://leetcode.com/problems/encode-and-decode-strings/

Design an algorithm to encode a list of strings to a single string and decode it back to the list of strings.

Constraints:
- 0 <= strs.length < 100
- 0 <= strs[i].length < 200
- strs[i] contains any possible characters out of 256 valid ascii characters.

Example 1:
Input: strs = ["lint","code","love","you"]
Output: ["lint","code","love","you"]

Example 2:
Input: strs = [""]
Output: [""]
"""
class Codec:
    def encode(self, strs):
        return ''.join(f'{len(s)}#{s}' for s in strs)
    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res

# Example usage:
if __name__ == "__main__":
    codec = Codec()
    strs = ["lint","code","love","you"]
    encoded = codec.encode(strs)
    print(encoded)
    print(codec.decode(encoded))  # Output: ['lint','code','love','you']
    print(codec.decode(codec.encode([""])))  # Output: ['']
