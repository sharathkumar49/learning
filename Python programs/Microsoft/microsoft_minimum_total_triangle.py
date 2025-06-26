# Microsoft: Find the minimum path sum in a triangle (DP)
def minimum_total(triangle):
    dp = triangle[-1][:]
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
    return dp[0]

if __name__ == "__main__":
    n = int(input("Number of rows: "))
    triangle = [list(map(int, input().split())) for _ in range(n)]
    print("Minimum path sum:", minimum_total(triangle))
