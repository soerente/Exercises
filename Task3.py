"""
A palindrome is a sequence of characters that reads the same backwards and forwards.
Given a string, s, find the longest palindromic substring in s.

Example:
Input: "banana"
Output: "anana"
Input: "million"
Output: "illi"
"""

# Approach (Dynamic Programming), Time Complexity: O(n^2), n = len(s)
class Solution:
    def longestPalindrome(self, s):
        #Fill this in
        n = len(s)
        pal = []
        max_pal = s[0]

        for i in range(n):
            pal.append([0]*n)
            pal[i][i] = 1                            # palindromic substring of length 1
            if i+1 < n and s[i] == s[i+1]:
                pal[i][i+1] = 1                      # palindromic substring of length 2
                max_pal = s[i:i+2]

        for j in range(2,n):
            for i in range(n-j):
                if s[i] == s[i+j] and pal[i+1][i+j-1] == 1:
                    pal[i][i+j] = 1                  # palindromic substring of length j+1
                    max_pal = s[i:i+j+1]

        return max_pal

s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar