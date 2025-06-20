"""
901. Online Stock Span
https://leetcode.com/problems/online-stock-span/

Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.
The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the price of the stock was less than or equal to today's price.

Implement the StockSpanner class:
- StockSpanner() Initializes the object of the class.
- int next(int price) Returns the span of the stock's price given that today's price is price.

Constraints:
- 1 <= price <= 10^5
- At most 10^4 calls will be made to next.

Example:
Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
"""
class StockSpanner:
    def __init__(self):
        self.stack = []  # pair: (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span

# Example usage
if __name__ == "__main__":
    sp = StockSpanner()
    print(sp.next(100))  # Output: 1
    print(sp.next(80))   # Output: 1
    print(sp.next(60))   # Output: 1
    print(sp.next(70))   # Output: 2
    print(sp.next(60))   # Output: 1
    print(sp.next(75))   # Output: 4
    print(sp.next(85))   # Output: 6
