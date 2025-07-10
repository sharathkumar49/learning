# Check if two strings are anagrams
def are_anagrams(s1, s2):
    return sorted(s1.replace(' ', '').lower()) == sorted(s2.replace(' ', '').lower())

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


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))