# Amazon: Top K Frequent Elements
def top_k_frequent(nums, k):
    from collections import Counter
    return [item for item, _ in Counter(nums).most_common(k)]

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    k = int(input("Top k: "))
    print("Top k frequent:", top_k_frequent(nums, k))
