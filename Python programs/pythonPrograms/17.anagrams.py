def sort_string(s):
    return ''.join(sorted(s)) 

def are_anagrams(str1, str2):
    return sort_string(str1) == sort_string(str2)

def group_anagrams(words):
    used = [False] * len(words)
    result = []
    
    for i in range(len(words)):
        if not used[i]:
            anagram_group = [words[i]]
            used[i] = True
            for j in range(i + 1, len(words)):
                if not used[j] and are_anagrams(words[i], words[j]):
                    anagram_group.append(words[j])
                    used[j] = True
            result.append(anagram_group)
    
    return result

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagram_groups = group_anagrams(words)
print(anagram_groups)

