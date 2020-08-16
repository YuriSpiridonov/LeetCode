"""
    Given a sorted linked list, delete all duplicates such that each element 
    appear only once.

    Example:
    Input: 1->1->2->3->3
    Output: 1->2->3
"""
#Difficulty: Easy
#165 / 165 test cases passed.
#Runtime: 40 ms
#Memory Usage: 13.9 MB

#Runtime: 40 ms, faster than 87.68% of Python3 online submissions for Remove Duplicates from Sorted List.
#Memory Usage: 13.9 MB, less than 31.86% of Python3 online submissions for Remove Duplicates from Sorted List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        prev = head
        curr = head.next
        while curr:
            if prev.val != curr.val:
                prev = curr
                curr = curr.next
            else:
                while prev.val == curr.val:
                    curr = curr.next
                    if not curr:
                        prev.next = None
                        break
                prev.next = curr
        return head
