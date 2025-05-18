
#Recursive approach
def get_permutations(s):
    if len(s) <= 1:
        return [s]

    permutations = []
    for i, char in enumerate(s):
        print("i, char:", i, char)
        remaining = s[:i] + s[ i +1:]
        print("remaining: ", remaining)
        for sub_perm in get_permutations(remaining):
            print("permutations to append: ", char, sub_perm)
            permutations.append(char + sub_perm)

    return permutations

print(get_permutations('abc'))


#
# #Iterative Approach
# from collections import deque
#
# def iterative_permutations(s):
#     """Generate permutations iteratively using a queue."""
#     queue = deque([""])  # Start with an empty string
#     for char in s:
#         for _ in range(len(queue)):
#             current = queue.popleft()
#             for i in range(len(current) + 1):
#                 queue.append(current[:i] + char + current[i:])
#     return list(queue)
#
# # Example usage
# print(iterative_permutations("abc"))
#
#
# # Iterative approach without using queue
# def iterative_permutations_withoutqueue(s):
#     """Generate all permutations iteratively using a list."""
#     permutations = [""]  # Start with an empty string
#
#     for char in s:
#         new_permutations = []
#         for perm in permutations:
#             for i in range(len(perm) + 1):  # Insert char at every position
#                 new_permutations.append(perm[:i] + char + perm[i:])
#         permutations = new_permutations  # Update permutations list
#
#     return permutations
#
# # Example usage
# print(iterative_permutations_withoutqueue("abc"))
#
#
#
# # Using Backtracking
# def backtrack_permutations(s, l, r):
#     """Generate permutations using backtracking."""
#     if l == r:
#         print("".join(s))  # Output each permutation
#     else:
#         for i in range(l, r):
#             s[l], s[i] = s[i], s[l]  # Swap
#             backtrack_permutations(s, l + 1, r)
#             s[l], s[i] = s[i], s[l]  # Swap back (backtrack)
#
# # Example usage
# input_str = list("abc")
# backtrack_permutations(input_str, 0, len(input_str))
