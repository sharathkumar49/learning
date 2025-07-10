"""
LeetCode 1472. Design Browser History

Design a browser history system. Implement the BrowserHistory class:
- BrowserHistory(string homepage): Initializes the object with the homepage of the browser.
- void visit(string url): Visits url from the current page. It clears up all the forward history.
- string back(int steps): Move steps back in history. Return the current url after moving back in history at most steps.
- string forward(int steps): Move steps forward in history. Return the current url after moving forward in history at most steps.

Constraints:
- 1 <= homepage.length <= 20
- 1 <= url.length <= 20
- 1 <= steps <= 100
- At most 5000 calls will be made to visit, back, and forward.

Example:
Input: ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"], [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output: [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]
"""
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.curr+1]
        self.history.append(url)
        self.curr += 1

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(len(self.history)-1, self.curr + steps)
        return self.history[self.curr]

# Example usage:
# browser = BrowserHistory("leetcode.com")
# browser.visit("google.com")
# browser.visit("facebook.com")
# browser.visit("youtube.com")
# print(browser.back(1))  # Output: facebook.com
