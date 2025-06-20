"""
LeetCode 726. Number of Atoms

Given a string formula representing a chemical formula, return the count of each atom.

Example 1:
Input: formula = "H2O"
Output: "H2O"

Example 2:
Input: formula = "Mg(OH)2"
Output: "H2MgO2"

Example 3:
Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"

Constraints:
- 1 <= formula.length <= 1000
- formula consists of English letters, digits, '(', and ')'.
- formula is always valid.
"""
def countOfAtoms(formula: str) -> str:
    import collections
    def parse():
        n = len(formula)
        stack = [collections.Counter()]
        i = 0
        while i < n:
            if formula[i] == '(': 
                stack.append(collections.Counter())
                i += 1
            elif formula[i] == ')':
                i += 1
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                mult = int(formula[i_start:i] or 1)
                top = stack.pop()
                for name in top:
                    stack[-1][name] += top[name] * mult
            else:
                i_start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                name = formula[i_start:i]
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                mult = int(formula[i_start:i] or 1)
                stack[-1][name] += mult
        return stack[0]
    count = parse()
    return ''.join(name + (str(count[name]) if count[name] > 1 else '') for name in sorted(count))

# Example usage
if __name__ == "__main__":
    print(countOfAtoms("H2O"))            # Output: "H2O"
    print(countOfAtoms("Mg(OH)2"))        # Output: "H2MgO2"
    print(countOfAtoms("K4(ON(SO3)2)2"))  # Output: "K4N2O14S4"
