

reverse = lambda s: s if len(s) <= 1 else reverse(s[1:]) + s[0]
print(reverse("hello"))  # Output: "olleh"

