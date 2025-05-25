# Word ladder (shortest transformation sequence)
from collections import deque

def word_ladder(begin, end, word_list):
    word_set = set(word_list)
    q = deque([(begin, 1)])
    while q:
        word, steps = q.popleft()
        if word == end:
            return steps
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in word_set:
                    word_set.remove(next_word)
                    q.append((next_word, steps+1))
    return 0

if __name__ == "__main__":
    begin = input("Begin word: ")
    end = input("End word: ")
    word_list = input("Word list (space separated): ").split()
    print("Length:", word_ladder(begin, end, word_list))
