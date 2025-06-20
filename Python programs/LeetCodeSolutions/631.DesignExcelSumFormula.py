"""
631. Design Excel Sum Formula
Difficulty: Hard

Design the basic Excel sum formula. Implement the Excel class:
- Excel(height, width): Initializes the object with the height and width of the Excel sheet.
- set(row, column, val): Sets the cell at (row, column) to val.
- get(row, column): Returns the value at (row, column).
- sum(row, column, numbers): Sets the cell at (row, column) to be the sum of the cells indicated by numbers and returns the sum.

Example:
Input: ["Excel","set","sum","set","get"]
[[3,"C"],[1,"A",2],[3,"C",["A1","A1:B2"]],[2,"B",2],[3,"C"]]
Output: [null,null,4,null,6]

Constraints:
1 <= height, width <= 26
1 <= row <= height
'A' <= column <= 'Z'
0 <= val <= 100
0 <= numbers.length <= 5 * height * width
"""

class Excel:
    def __init__(self, height: int, width: str):
        self.h = height
        self.w = ord(width) - ord('A') + 1
        self.grid = [[0]*self.w for _ in range(self.h)]
        self.formula = {}
    def set(self, r: int, c: str, v: int):
        self.grid[r-1][ord(c)-ord('A')] = v
        self.formula.pop((r, c), None)
    def get(self, r: int, c: str) -> int:
        if (r, c) in self.formula:
            return self.sum(r, c, self.formula[(r, c)])
        return self.grid[r-1][ord(c)-ord('A')]
    def sum(self, r: int, c: str, numbers: list) -> int:
        cells = []
        for s in numbers:
            if ':' in s:
                start, end = s.split(':')
                sr, sc = int(start[1:]), ord(start[0])
                er, ec = int(end[1:]), ord(end[0])
                for rr in range(sr, er+1):
                    for cc in range(sc, ec+1):
                        cells.append((rr, chr(cc)))
            else:
                cells.append((int(s[1:]), s[0]))
        self.formula[(r, c)] = numbers
        total = sum(self.get(rr, cc) for rr, cc in cells)
        self.grid[r-1][ord(c)-ord('A')] = total
        return total

# Example usage
# excel = Excel(3, 'C')
# excel.set(1, 'A', 2)
# print(excel.sum(3, 'C', ['A1', 'A1:B2']))  # Output: 4
# excel.set(2, 'B', 2)
# print(excel.get(3, 'C'))  # Output: 6
