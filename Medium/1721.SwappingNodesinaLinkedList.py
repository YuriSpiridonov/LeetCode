'''
    You are given the head of a linked list, and an integer k.

    Return the head of the linked list after swapping the 
    values of the kth node from the beginning and the kth 
    node from the end (the list is 1-indexed).

    Example:
    Input: head = [1,2,3,4,5], k = 2
    Output: [1,4,3,2,5]

    Example:
    Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
    Output: [7,9,6,6,8,7,3,0,9,5]

    Example:
    Input: head = [1], k = 1
    Output: [1]

    Example:
    Input: head = [1,2], k = 1
    Output: [2,1]

    Example:
    Input: head = [1,2,3], k = 2
    Output: [1,2,3]

    Constraints:
        - The number of nodes in the list is n.
        - 1 <= k <= n <= 10^5
        - 0 <= Node.val <= 100
'''
#Difficulty: Medium
#132 / 132 test cases passed.
#Runtime: 5504 ms
#Memory Usage: 49.6 MB

#Runtime: 5504 ms, faster than 100.00% of Python3 online submissions for Swapping Nodes in a Linked List.
#Memory Usage: 49.6 MB, less than 100.00% of Python3 online submissions for Swapping Nodes in a Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        queue = []
        while head:
            queue.append(head)
            head = head.next
        queue[k-1], queue[-k] = queue[-k], queue[k-1]
        head = queue.pop(0)
        node = head
        while queue:
            node.next = queue.pop(0)
            node = node.next
        node.next = None
        return head
