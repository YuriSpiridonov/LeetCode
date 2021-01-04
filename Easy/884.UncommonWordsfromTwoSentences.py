'''
    We are given two sentences A and B.  (A sentence is a 
    string of space separated words.  Each word consists 
    only of lowercase letters.)

    A word is uncommon if it appears exactly once in one 
    of the sentences, and does not appear in the other 
    sentence.

    Return a list of all uncommon words. 

    You may return the list in any order.

    Example:
    Input: A = "this apple is sweet", B = "this apple is sour"
    Output: ["sweet","sour"]

    Example:
    Input: A = "apple apple", B = "banana"
    Output: ["banana"]

    Note:
        1. 0 <= A.length <= 200
        2. 0 <= B.length <= 200
        3. A and B both contain only spaces and lowercase 
           letters.
'''
#Difficulty: Easy
#53 / 53 test cases passed.
#Runtime: 20 ms
#Memory Usage: 14.1 MB

#Runtime: 20 ms, faster than 98.73% of Python3 online submissions for Uncommon Words from Two Sentences.
#Memory Usage: 14.1 MB, less than 91.89% of Python3 online submissions for Uncommon Words from Two Sentences.

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        B = f'{A} {B}'.split(' ')
        A = set(B)
        return [a for a in A if B.count(a) == 1]
