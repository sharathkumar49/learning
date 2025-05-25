# File read/write and word count
def word_count(filename):
    with open(filename, 'r') as f:
        text = f.read()
    words = text.split()
    return len(words)

def write_file(filename, text):
    with open(filename, 'w') as f:
        f.write(text)

if __name__ == "__main__":
    fname = input("Filename: ")
    text = input("Text to write: ")
    write_file(fname, text)
    print("Word count:", word_count(fname))
