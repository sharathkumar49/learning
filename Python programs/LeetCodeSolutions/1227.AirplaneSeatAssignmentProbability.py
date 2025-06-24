"""
1227. Airplane Seat Assignment Probability

Given n passengers and n seats, the first passenger picks a random seat, each subsequent passenger takes their seat if available, otherwise a random seat. Return the probability that the last passenger gets their seat.

Constraints:
- 1 <= n <= 10^5

Example:
Input: n = 1
Output: 1.0

"""
def nthPersonGetsNthSeat(n):
    return 1.0 if n == 1 else 0.5

# Example usage
if __name__ == "__main__":
    print(nthPersonGetsNthSeat(1))  # Output: 1.0
    print(nthPersonGetsNthSeat(2))  # Output: 0.5
