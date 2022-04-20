"""
Add two numbers as a linked list:
You are given two linked-lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807
"""

# Definition for singly-linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# First Approach (Double Digit Addition), Time Complexity: O(n), n=max(|nodes l1|,|nodes l2|)
class Solution(object):
    def addTwoNumbers(self, l1, l2, c=0):
        # Fill this in
        head = None

        while l1 or l2:
            num = (0 if not l1 else l1.val) + (0 if not l2 else l2.val) + c

            c = 0
            if num >= 10:
                num = num % 10
                c = 1

            if head:
                node.next = ListNode(num)
                node = node.next
            else:
                head = ListNode(num)
                node = head

            l1 = (None if not l1 else l1.next)
            l2 = (None if not l2 else l2.next)

        if c==1: node.next = ListNode(1)

        return head


# Second Approach (Convert to String), Time Complexity: O(n), n=max(|nodes l1|,|nodes l2|)
class Solution2(object):
    def addTwoNumbers(self, l1, l2, c=0):
        # Fill this in
        first_num = ""
        while l1:
            first_num += str(l1.val)
            l1 = l1.next

        second_num = ""
        while l2:
            second_num += str(l2.val)
            l2 = l2.next

        first_num = first_num[::-1]
        second_num = second_num[::-1]

        num = int(first_num) + int(second_num)
        num = str(num)[::-1]

        head = ListNode(int(num[c]))
        node = head
        c += 1
        while c < len(num):
            node.next = ListNode(int(num[c]))
            node = node.next
            c += 1

        return head


# Input Example
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next
# 7 0 8