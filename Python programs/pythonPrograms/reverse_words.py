# Reverse words in a sentence
def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

if __name__ == "__main__":
    s = input("Enter a sentence: ")
    print("Reversed:", reverse_words(s))
