# Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '['  ']’. 
# These brackets must be close in the correct order. for example "()" and "()[]{}" are valid 
# but "[)", "({[)]" and "{{{" are invalid. i maybe understand

class BracketValidator:
    def __init__(self, string):
        self.string = string

    def isValid(self):
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in self.string:
            if char in bracket_map.values():  # opening brackets
                stack.append(char)
            elif char in bracket_map:  # closing brackets
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                # Invalid character (optional to allow or disallow)
                return False

        return len(stack) == 0