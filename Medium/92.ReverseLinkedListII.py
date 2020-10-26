"""
    Reverse a linked list from position m to n. Do it in one-pass.

    Note: 1 ≤ m ≤ n ≤ length of list.

    Example:
    Input: 1->2->3->4->5->NULL, m = 2, n = 4
    Output: 1->4->3->2->5->NULL
"""
#Difficulty: Medium
#44 / 44 test cases passed.
#Runtime: 24 ms
#Memory Usage: 14.2 MB

#Runtime: 24 ms, faster than 95.46% of Python3 online submissions for Reverse Linked List II.
#Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Reverse Linked List II.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        count = 1
        node = head
        stack = []
        while count != m:
            node = node.next
            count += 1
        reverse = node
        while count <= n:
            stack.append(reverse.val)
            reverse = reverse.next
            count += 1
        while stack:
            node.val = stack.pop()
            node = node.next
        return head
