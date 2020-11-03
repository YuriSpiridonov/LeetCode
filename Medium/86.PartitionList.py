"""
    Given a linked list and a value x, partition it such that all nodes less 
    than x come before nodes greater than or equal to x.

    You should preserve the original relative order of the nodes in each of 
    the two partitions.

    Example:
    Input: head = 1->4->3->2->5->2, x = 3
    Output: 1->2->2->4->3->5
"""
#Difficulty: Medium
#166 / 166 test cases passed.
#Runtime: 36 ms
#Memory Usage: 14.2 MB

#Runtime: 36 ms, faster than 57.43% of Python3 online submissions for Partition List.
#Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Partition List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left = [0]
        right = []
        curr = head
        while curr:
            if curr.val < x:
                left.append(curr.val)
            else:
                right.append(curr.val)
            curr = curr.next
        left.extend(right)
        head = ListNode(left.pop(0))
        node = head
        while left:
            node.next = ListNode(left.pop(0))
            node = node.next
        return head.next
