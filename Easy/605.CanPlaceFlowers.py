"""
    You have a long flowerbed in which some of the plots are planted, 
    and some are not. However, flowers cannot be planted in adjacent plots.

    Given an integer array flowerbed containing 0's and 1's, where 0 means 
    empty and 1 means not empty, and an integer n, return if n new flowers 
    can be planted in the flowerbed without violating 
    the no-adjacent-flowers rule.

    Example:
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true

    Example:
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false

    Constraints:
        - 1 <= flowerbed.length <= 2 * 10^4
        - flowerbed[i] is 0 or 1.
        - There are no two adjacent flowers in flowerbed.
        - 0 <= n <= flowerbed.length
"""
#Difficulty: Easy
#123 / 123 test cases passed.
#Runtime: 168 ms
#Memory Usage: 14.5 MB

#Runtime: 168 ms, faster than 41.51% of Python3 online submissions for Can Place Flowers.
#Memory Usage: 14.5 MB, less than 66.37% of Python3 online submissions for Can Place Flowers.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for x in flowerbed:
            if x == 0:
                count += 1
            else: 
                count = 0
            if count == 3:
                n -= 1
                count = 1
            if not n:
                break
        return not n
