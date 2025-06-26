# Microsoft: Merge Intervals
# Given a collection of intervals, merge all overlapping intervals.

def merge(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for curr in intervals[1:]:
        if curr[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], curr[1])
        else:
            merged.append(curr)
    return merged

if __name__ == "__main__":
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    print(merge(intervals1))  # Output: [[1,6],[8,10],[15,18]]
    intervals2 = [[1,4],[4,5]]
    print(merge(intervals2))  # Output: [[1,5]]
