'''
    You are given an array of k linked-lists lists, each 
    linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list 
    and return it.

    Example:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
                 [
                 1->4->5,
                 1->3->4,
                 2->6
                 ]
                 merging them into one sorted list:
                 1->1->2->3->4->4->5->6

    Example:
    Input: lists = []
    Output: []

    Example:
    Input: lists = [[]]
    Output: []

    Constraints:
        - k == lists.length
        - 0 <= k <= 10^4
        - 0 <= lists[i].length <= 500
        - -10^4 <= lists[i][j] <= 10^4
        - lists[i] is sorted in ascending order.
        - The sum of lists[i].length won't exceed 10^4.
'''
#Difficulty: Hard
#133 / 133 test cases passed.
#Runtime: 92 ms
#Memory Usage: 18.3 MB

#Runtime: 92 ms, faster than 93.83% of Python3 online submissions for Merge k Sorted Lists.
#Memory Usage: 18.3 MB, less than 27.03% of Python3 online submissions for Merge k Sorted Lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode()
        node = head
        nodes = []
        for l_list in lists:
            while l_list:
                nodes.append(l_list.val)
                l_list = l_list.next
        for val in sorted(nodes):
            node.next = ListNode(val)
            node = node.next
        return head.next