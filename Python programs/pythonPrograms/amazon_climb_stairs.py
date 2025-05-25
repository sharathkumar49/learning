# Amazon: Find the number of ways to climb stairs (DP)
def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    n = int(input("Number of stairs: "))
    print("Ways to climb:", climb_stairs(n))
