"""
Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x.
Return -1 if the target is not found.

Example:
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]
Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]
"""

# First Approach (Binary Tree), Time Complexity: O(log n), n = len(arr)
class Solution:
  def getRange(self, arr, target):
    # Fill this in.
    fir = sec = -1

    l = 0
    r = len(arr)-1
    while l < r:
        i = (l+r)//2
        if target <= arr[i]: r = i
        else: l = i+1
    if target == arr[l]: fir = l

    l = 0
    r = len(arr)-1
    while l < r:
        i = (l+r)//2
        if target >= arr[i+1]: l = i+1
        else: r = i
    if target == arr[l]: sec = l

    return [fir, sec]


# Second Approach (Slicing), Time Complexity: O(n), n = len(arr)
class Solution2:
  def getRange(self, arr, target):
    # Fill this in.
    try:
        return [arr.index(target), len(arr)-1-arr[::-1].index(target)]
    except ValueError:
        return [-1,-1]


arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]