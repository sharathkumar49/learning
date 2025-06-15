
# Longest Streak in a List
def longest_streak(lst):
    max_streak = []
    current_streak = []

    for num in lst:
        if not current_streak or num > current_streak[-1]:
            current_streak.append(num)
        else:
            if len(current_streak) > len(max_streak):
                max_streak = current_streak
            current_streak = [num]

    if len(current_streak) > len(max_streak):
        max_streak = current_streak

    return max_streak

# Example usage
numbers = [1, 2, 3, 2, 5, 6, 7, 8, 4, 5]
result = longest_streak(numbers)
print("Longest Streak:", result)