"""
    Remove all elements from a linked list of integers that have value val.

    Example:
    Input:  1->2->6->3->4->5->6, val = 6
    Output: 1->2->3->4->5
"""
#Difficulty: Easy
#65 / 65 test cases passed.
#Runtime: 68 ms
#Memory Usage: 16.9 MB

#Runtime: 68 ms, faster than 88.02% of Python3 online submissions for Remove Linked List Elements.
#Memory Usage: 16.9 MB, less than 56.57% of Python3 online submissions for Remove Linked List Elements.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head: 
            if head.val == val:
                head = head.next
            else:
                break
        if not head:
            return        
        node = head
        while node:
            if node.val == val:
                if node.next:
                    node.val = node.next.val
                    node.next = node.next.next
                    continue
                else:
                    prev.next = None
            if not node.next:
                return head
            prev = node
            node = node.next
