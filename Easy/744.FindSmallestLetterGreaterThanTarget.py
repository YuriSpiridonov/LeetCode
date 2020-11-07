"""
    Given a list of sorted characters letters containing only lowercase 
    letters, and given a target letter target, find the smallest element 
    in the list that is larger than the given target.

    Letters also wrap around. For example, if the target is target = 'z'
    and letters = ['a', 'b'], the answer is 'a'.

    Examples:
    Input:
    letters = ["c", "f", "j"]
    target = "a"
    Output: "c"

    Input:
    letters = ["c", "f", "j"]
    target = "c"
    Output: "f"

    Input:
    letters = ["c", "f", "j"]
    target = "d"
    Output: "f"

    Input:
    letters = ["c", "f", "j"]
    target = "g"
    Output: "j"

    Input:
    letters = ["c", "f", "j"]
    target = "j"
    Output: "c"

    Input:
    letters = ["c", "f", "j"]
    target = "k"
    Output: "c"

    Note:
        1. letters has a length in range [2, 10000].
        2. letters consists of lowercase letters, and contains at least 2 
           unique letters.
        3. target is a lowercase letter.
"""
#Difficulty: Easy
#165 / 165 test cases passed.
#Runtime: 104 ms
#Memory Usage: 14.4 MB

#Runtime: 104 ms, faster than 89.09% of Python3 online submissions for Find Smallest Letter Greater Than Target.
#Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Find Smallest Letter Greater Than Target.

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters) - 1
        if letters[-1] <= target:
            return letters[l]
        while l < r:
            m = (l+r) // 2
            if letters[m] > target:
                r = m
            else:
                l = m + 1
        return letters[l]
