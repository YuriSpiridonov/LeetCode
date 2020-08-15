"""
    Given a linked list, remove the n-th node from the end of list and return 
    its head.

    Example:
    Given linked list: 1->2->3->4->5, and n = 2.
    After removing the second node from the end, the linked list becomes 
                                                                    1->2->3->5.

    Note:
        Given n will always be valid.
    Follow up:
        Could you do this in one pass?
"""
#Difficulty: Medium
#208 / 208 test cases passed.
#Runtime: 32 ms
#Memory Usage: 13.9 MB

#Runtime: 32 ms, faster than 81.09% of Python3 online submissions for Remove Nth Node From End of List.
#Memory Usage: 13.9 MB, less than 40.68% of Python3 online submissions for Remove Nth Node From End of List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        stack = []
        i = 1
        while node:
            stack.append(node)
            node = node.next
        if n == 1:
            stack.pop()
            if stack:
                stack.pop().next = None
            else:
                head = None
            return head
        if n == len(stack):
            head = stack.pop(1)
            return head
        while True:
            if i != n:
                prev = stack.pop()
            elif i == n:
                stack.pop(-2).next = prev
                return head
            i += 1
