# Count set bits in integer
def count_set_bits(n):
    count = 0
    while n:
        n &= n-1
        count += 1
    return count

if __name__ == "__main__":
    n = int(input("Enter integer: "))
    print("Set bits:", count_set_bits(n))
