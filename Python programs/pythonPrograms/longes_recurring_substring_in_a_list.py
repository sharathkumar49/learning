def get_substrings(word):
    substrings = {}
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            substrings[word[i:j]] = substrings.get(word[i:j], 0) + 1
    return substrings


def find_longest_common_substring(keywords):
    substring_counts = {}

    for word in keywords:
        substrings = get_substrings(word)
        for sub in substrings:
            if sub in substring_counts:
                substring_counts[sub] += 1
            else:
                substring_counts[sub] = 1

    common_substrings = [sub for sub in substring_counts if substring_counts[sub] > 1]
    return max(common_substrings, key=len, default="")

keywords = ['milk', 'catalog', 'c+', 'python', 'cat', 'dog', 'cashless', 'encashment']
result = find_longest_common_substring(keywords)
print(result)  #cash 
