'''
    You are given a string s of even length. Split this 
    string into two halves of equal lengths, and let a be 
    the first half and b be the second half.

    Two strings are alike if they have the same number of 
    vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). 
    Notice that s contains uppercase and lowercase letters.

    Return true if a and b are alike. Otherwise, return false.

    Example:
    Input: s = "book"
    Output: true
    Explanation: a = "bo" and b = "ok". a has 1 vowel and b 
                 has 1 vowel. Therefore, they are alike.

    Example:
    Input: s = "textbook"
    Output: false
    Explanation: a = "text" and b = "book". a has 1 vowel 
                 whereas b has 2. Therefore, they are not 
                 alike.
                 Notice that the vowel o is counted twice.

    Example:
    Input: s = "MerryChristmas"
    Output: false

    Example:
    Input: s = "AbCdEfGh"
    Output: true

    Constraints:
        - 2 <= s.length <= 1000
        - s.length is even.
        - s consists of uppercase and lowercase letters.
'''
#Difficulty: Easy
#113 / 113 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.4 MB

#Runtime: 32 ms, faster than 87.87% of Python3 online submissions for Determine if String Halves Are Alike.
#Memory Usage: 14.4 MB, less than 40.73% of Python3 online submissions for Determine if String Halves Are Alike.

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = 0
        b = 0
        s = s.lower()
        vowels = 'aeiou'
        length = len(s)//2
        for char in vowels:
            a += s[:length].count(char) 
            b += s[length:].count(char)
        return a == b
