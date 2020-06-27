"""
    Given the array candies and the integer extraCandies, where candies[i] 
    represents the number of candies that the ith kid has.

    For each kid check if there is a way to distribute extraCandies among the 
    kids such that he or she can have the greatest number of candies among them. 
    Notice that multiple kids can have the greatest number of candies.

    Example:
    Input: candies = [2,3,5,1,3], extraCandies = 3
    Output: [true,true,true,false,true] 

    Explanation: 
                - Kid 1 has 2 candies and if he or she receives all extra 
                  candies (3) will have 5 candies --- the greatest number of 
                  candies among the kids. 
                - Kid 2 has 3 candies and if he or she receives at least 2 
                  extra candies will have the greatest number of candies among 
                  the kids. 
                - Kid 3 has 5 candies and this is already the greatest number 
                  of candies among the kids. 
                - Kid 4 has 1 candy and even if he or she receives all extra 
                  candies will only have 4 candies. 
                - Kid 5 has 3 candies and if he or she receives at least 2 
                  extra candies will have the greatest number of candies among 
                  the kids. 

    Constraints:
        - 2 <= candies.length <= 100
        - 1 <= candies[i] <= 100
        - 1 <= extraCandies <= 50
"""
#Difficulty: Easy
#103 / 103 test cases passed.
#Runtime: 40 ms
#Memory Usage: 13.6 MB

#Runtime: 40 ms, faster than 53.31% of Python3 online submissions for Kids With the Greatest Number of Candies.
#Memory Usage: 13.6 MB, less than 93.94% of Python3 online submissions for Kids With the Greatest Number of Candies.

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [currentCandies + extraCandies >= max(candies) for currentCandies in candies]

#Runtime: 36 ms, faster than 77.12% of Python3 online submissions for Kids With the Greatest Number of Candies.
#Memory Usage: 13.9 MB, less than 41.50% of Python3 online submissions for Kids With the Greatest Number of Candies 

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        return [currentCandies + extraCandies >= maxCandies for currentCandies in candies]
