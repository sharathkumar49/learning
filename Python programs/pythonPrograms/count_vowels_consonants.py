# Count vowels and consonants in a string
def count_vowels_consonants(s):
    vowels = set('aeiouAEIOU')
    v = c = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    return v, c

if __name__ == "__main__":
    s = input("Enter a string: ")
    v, c = count_vowels_consonants(s)
    print(f"Vowels: {v}, Consonants: {c}")
