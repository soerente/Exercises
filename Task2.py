"""
Given a string, find the length of the longest substring without repeating characters.
"""

# Approach (Dynamic Programming), Time Complexity: O(n), n = len(s)
class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in
    num = [1]
    chars = {s[0]}

    for i,c in enumerate(s[1:]):
        if c in chars:
          chars.clear()
          chars.add(c)
          num.append(1)
        else:
          chars.add(c)
          num.append(num[i]+1)

    return max(num)

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
