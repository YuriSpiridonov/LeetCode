"""
    Given a sorted linked list, delete all nodes that have duplicate numbers, 
    leaving only distinct numbers from the original list.

    Return the linked list sorted as well.

    Example:
    Input: 1->2->3->3->4->4->5
    Output: 1->2->5

    Example:
    Input: 1->1->1->2->3
    Output: 2->3
"""
#Difficulty: Medium
#166 / 166 test cases passed.
#Runtime: 48 ms
#Memory Usage: 13.9 MB

#Runtime: 48 ms, faster than 17.44% of Python3 online submissions for Remove Duplicates from Sorted List II.
#Memory Usage: 13.9 MB, less than 99.96% of Python3 online submissions for Remove Duplicates from Sorted List II.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        visited = []
        pop = []
        node = head
        while node:
            if node.val not in visited:
                visited.append(node.val)
            else:
                pop.append(node.val)
            node = node.next
        new_head = ListNode()
        prev = new_head
        curr = head
        while curr:
            if curr.val not in pop:
                prev.next = curr
                prev = prev.next
            curr = curr.next
        prev.next = None
        return new_head.next
