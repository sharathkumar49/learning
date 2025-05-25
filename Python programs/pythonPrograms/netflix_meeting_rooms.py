# Netflix: Meeting rooms (can attend all meetings)
def can_attend(meetings):
    meetings.sort()
    for i in range(1, len(meetings)):
        if meetings[i][0] < meetings[i-1][1]:
            return False
    return True

if __name__ == "__main__":
    n = int(input("Number of meetings: "))
    meetings = [tuple(map(int, input().split())) for _ in range(n)]
    print("Can attend all meetings:", can_attend(meetings))
