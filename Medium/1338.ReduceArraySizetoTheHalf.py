"""
    Given an array arr.  You can choose a set of integers and remove all the 
    occurrences of these integers in the array.

    Return the minimum size of the set so that at least half of the integers of
    the array are removed.

    Example:
    Input: arr = [3,3,3,3,5,5,5,2,2,7]
    Output: 2
    Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has 
                 size 5 (i.e equal to half of the size of the old array).
                 Possible sets of size 2 are {3,5},{3,2},{5,2}.
                 Choosing set {2,7} is not possible as it will make the new 
                 array [3,3,3,3,5,5,5] which has size greater than half of the 
                 size of the old array.

    Example:
    Input: arr = [7,7,7,7,7,7]
    Output: 1
    Explanation: The only possible set you can choose is {7}. This will make 
                 the new array empty.

    Example:
    Input: arr = [1,9]
    Output: 1

    Example:
    Input: arr = [1000,1000,3,7]
    Output: 1

    Example:
    Input: arr = [1,2,3,4,5,6,7,8,9,10]
    Output: 5

    Constraints:
        - 1 <= arr.length <= 10^5
        - arr.length is even.
        - 1 <= arr[i] <= 10^5
"""
#Difficulty: Medium
#31 / 31 test cases passed.
#Runtime: 584 ms
#Memory Usage: 30.5 MB

#Runtime: 584 ms, faster than 98.64% of Python3 online submissions for Reduce Array Size to The Half.
#Memory Usage: 30.5 MB, less than 78.12% of Python3 online submissions for Reduce Array Size to The Half.

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        numbers = {}
        half = len(arr) // 2
        for number in arr:
            if number not in numbers:
                numbers[number] = 1
            else:
                numbers[number] += 1
        for index, value in enumerate(sorted(list(numbers.values()), reverse=True)):
            half -= value
            if half <= 0:
                return index + 1
