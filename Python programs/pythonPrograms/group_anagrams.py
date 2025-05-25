# Group Anagrams from a list of words
def group_anagrams(words):
    from collections import defaultdict
    groups = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        groups[key].append(word)
    return list(groups.values())

if __name__ == "__main__":
    words = input("Enter words (space separated): ").split()
    print("Grouped anagrams:", group_anagrams(words))
