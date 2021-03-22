'''
    Given a wordlist, we want to implement a spellchecker 
    that converts a query word into a correct word.

    For a given query word, the spell checker handles two 
    categories of spelling mistakes:

        - Capitalization: If the query matches a word in the 
          wordlist (case-insensitive), then the query word 
          is returned with the same case as the case in the 
          wordlist.
            = Example: wordlist = ["yellow"], 
              query = "YellOw": correct = "yellow"
            = Example: wordlist = ["Yellow"], 
              query = "yellow": correct = "Yellow"
            = Example: wordlist = ["yellow"], 
              query = "yellow": correct = "yellow"
        - Vowel Errors: If after replacing the vowels 
          ('a', 'e', 'i', 'o', 'u') of the query word with 
          any vowel individually, it matches a word in the 
          wordlist (case-insensitive), then the query word 
          is returned with the same case as the match in the 
          wordlist.
            = Example: wordlist = ["YellOw"], 
              query = "yollow": correct = "YellOw"
            = Example: wordlist = ["YellOw"], 
              query = "yeellow": correct = "" (no match)
            = Example: wordlist = ["YellOw"], 
              query = "yllw": correct = "" (no match)

    In addition, the spell checker operates under the 
    following precedence rules:

        - When the query exactly matches a word in the 
          wordlist (case-sensitive), you should return the 
          same word back.
        - When the query matches a word up to capitlization, 
          you should return the first such match in the 
          wordlist.
        - When the query matches a word up to vowel errors, 
          you should return the first such match in the 
          wordlist.
        - If the query has no matches in the wordlist, you 
          should return the empty string.

    Given some queries, return a list of words answer, where 
    answer[i] is the correct word for query = queries[i].

    Example:
    Input: wordlist = ["KiTe","kite","hare","Hare"], 
           queries = ["kite","Kite","KiTe","Hare","HARE",
                      "Hear","hear","keti","keet","keto"]
    Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

    Note:
        - 1 <= wordlist.length <= 5000
        - 1 <= queries.length <= 5000
        - 1 <= wordlist[i].length <= 7
        - 1 <= queries[i].length <= 7
        - All strings in wordlist and queries consist only 
          of english letters.
'''
#Difficulty: Medium
#53 / 53 test cases passed.
#Runtime: 164 ms
#Memory Usage: 16.9 MB

#Runtime: 164 ms, faster than 95.10% of Python3 online submissions for Vowel Spellchecker.
#Memory Usage: 16.9 MB, less than 73.06% of Python3 online submissions for Vowel Spellchecker.

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words_set = set(wordlist)
        words_book = {}
        words_mask = {}

        for word in wordlist:
            lower_word = word.lower()
            word_mask = self.replaceVowels(lower_word)
            if lower_word not in words_book:
                words_book[lower_word] = word
            if word_mask not in words_mask:
                words_mask[word_mask] = word

        for i, word in enumerate(queries):
            lower_word = word.lower()
            word_mask = self.replaceVowels(lower_word)
            if word not in words_set:
                if lower_word in words_book.keys():
                    queries[i] = words_book[lower_word]
                elif word_mask in words_mask.keys():
                    queries[i] = words_mask[word_mask]
                else:
                    queries[i] = ''
        return queries

    def replaceVowels(self, word):
        word = word.replace('a', '*')
        word = word.replace('e', '*')
        word = word.replace('i', '*')
        word = word.replace('o', '*')
        word = word.replace('u', '*')
        return word
