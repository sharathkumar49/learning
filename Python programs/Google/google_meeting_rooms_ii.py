# Google: Meeting Rooms II (min rooms required)
def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)
    s = e = used = 0
    while s < len(intervals):
        if starts[s] >= ends[e]:
            used -= 1
            e += 1
        used += 1
        s += 1
    return used

if __name__ == "__main__":
    n = int(input("Number of meetings: "))
    intervals = [list(map(int, input().split())) for _ in range(n)]
    print("Min rooms:", min_meeting_rooms(intervals))
