'''
    Given a linked list, reverse the nodes of a linked list 
    k at a time and return its modified list.

    k is a positive integer and is less than or equal to the 
    length of the linked list. If the number of nodes is not 
    a multiple of k then left-out nodes, in the end, should 
    remain as it is.

    Follow up:
        - Could you solve the problem in O(1) extra memory 
          space?
        - You may not alter the values in the list's nodes, 
          only nodes itself may be changed.

    Example:
            1 -> 2 -> 3 -> 4 -> 5 -> None
            2 -> 1 -> 4 -> 3 -> 5 -> None
    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]

    Example:
            1 -> 2 -> 3 -> 4 -> 5 -> None
            3 -> 2 -> 1 -> 4 -> 5 -> None
    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]

    Example:
    Input: head = [1,2,3,4,5], k = 1
    Output: [1,2,3,4,5]

    Example:
    Input: head = [1], k = 1
    Output: [1]

    Constraints:
        - The number of nodes in the list is in the range sz.
        - 1 <= sz <= 5000
        - 0 <= Node.val <= 1000
        - 1 <= k <= sz
'''
#Difficulty: Hard
#62 / 62 test cases passed.
#Runtime: 48 ms
#Memory Usage: 15.3 MB

#Runtime: 48 ms, faster than 77.08% of Python3 online submissions for Reverse Nodes in k-Group.
#Memory Usage: 15.3 MB, less than 45.70% of Python3 online submissions for Reverse Nodes in k-Group.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        stack = []
        new_head = ListNode()
        node = new_head
        i = 0
        while head:
            while i != k and head:
                i += 1
                stack.append(head)
                head = head.next
            while i == k and stack:
                node.next = stack.pop()
                node = node.next
                node.next = None
            i = 0
        if stack:
            node.next = stack.pop(0)
        return new_head.next