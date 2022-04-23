"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:
Input: "((()))"
Output: True
Input: "[()]{}"
Output: True
Input: "({[)]"
Output: False
"""

# Approach (Fill Stack), Time Complexity: O(n), n = len(s)
class Solution:
  def isValid(self, s):
    # Fill this in.
    if not s: return True
    if len(s) % 2 != 0 or s[0] in [')','}',']']: return False

    stack = [] # open bracket is followed by: another open bracket or closed bracket of the same type

    for p in s:
        if p in ['(','{','[']:
            stack.append(p)
        elif (p == ')' and stack[-1] == '(') or (p == '}' and stack[-1] == '{') or (p == ']' and stack[-1] == '['):
            stack.pop()
        else:
            return False

    if stack: return False
    else: return True

s = "()(){(())"
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))