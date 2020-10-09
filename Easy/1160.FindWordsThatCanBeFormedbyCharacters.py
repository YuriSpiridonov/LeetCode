"""
    You are given an array of strings words and a string chars.
    A string is good if it can be formed by characters from chars 
    (each character can only be used once).
    Return the sum of lengths of all good strings in words.

    Example:
    Input: words = ["cat","bt","hat","tree"], chars = "atach"
    Output: 6
    Explanation: 
                 The strings that can be formed are "cat" and "hat" so the 
                 answer is 3 + 3 = 6.

    Example:
    Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
    Output: 10
    Explanation: 
                 The strings that can be formed are "hello" and "world" so the 
                 answer is 5 + 5 = 10.

    Note:
        1. 1 <= words.length <= 1000
        2. 1 <= words[i].length, chars.length <= 100
        3. All strings contain lowercase English letters only.
"""
#Diffculty: Easy
#36 / 36 test cases passed.
#Runtime: 104 ms
#Memory Usage: 14.5 MB

#Runtime: 104 ms, faster than 87.77% of Python3 online submissions for Find Words That Can Be Formed by Characters.
#Memory Usage: 14.5 MB, less than 15.39% of Python3 online submissions for Find Words That Can Be Formed by Characters.

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        chrs = {}
        for char in chars:
            if char not in chrs:
                chrs[char] = 0
            chrs[char] += 1
        for word in words:
            letters = set(word)
            flag = True
            for letter in letters:
                if letter not in chrs or word.count(letter) > chrs[letter]:
                    flag = False
                    break
            if flag:
                count += len(word)
        return count
