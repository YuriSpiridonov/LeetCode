'''
    Given an array of strings products and a string searchWord. 
    We want to design a system that suggests at most three 
    product names from products after each character of 
    searchWord is typed. Suggested products should have common 
    prefix with the searchWord. If there are more than three 
    products with a common prefix return the three 
    lexicographically minimums products.

    Return list of lists of the suggested products after each 
    character of searchWord is typed. 

    Example:
    Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], 
           searchWord = "mouse"
    Output: [
            ["mobile","moneypot","monitor"],
            ["mobile","moneypot","monitor"],
            ["mouse","mousepad"],
            ["mouse","mousepad"],
            ["mouse","mousepad"]
            ]
    Explanation: products sorted lexicographically = 
                 ["mobile","moneypot","monitor","mouse","mousepad"]
                 After typing m and mo all products match and 
                 we show user ["mobile","moneypot","monitor"]
                 After typing mou, mous and mouse the system 
                 suggests ["mouse","mousepad"]

    Example:
    Input: products = ["havana"], 
           searchWord = "havana"
    Output: [
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"]
            ]

    Example:
    Input: products = ["bags","baggage","banner","box","cloths"], 
           searchWord = "bags"
    Output: [
            ["baggage","bags","banner"],
            ["baggage","bags","banner"],
            ["baggage","bags"],["bags"]
            ]

    Example:
    Input: products = ["havana"], 
           searchWord = "tatiana"
    Output: [[],[],[],[],[],[],[]]

    Constraints:
        - 1 <= products.length <= 1000
        - There are no repeated elements in products.
        - 1 <= Σ products[i].length <= 2 * 10^4
        - All characters of products[i] are lower-case 
          English letters.
        - 1 <= searchWord.length <= 1000
        - All characters of searchWord are lower-case 
          English letters.
'''
#Difficulty: Medium
#41 / 41 test cases passed.
#Runtime: 628 ms
#Memory Usage: 17 MB

#Runtime: 628 ms, faster than 19.59% of Python3 online submissions for Search Suggestions System.
#Memory Usage: 17 MB, less than 89.61% of Python3 online submissions for Search Suggestions System.

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        for i in range(1, len(searchWord)+1):
            temp = []
            for word in products:
                if word.startswith(searchWord[:i]):
                    temp.append(word)
                if 3 == len(temp):
                    break
            result.append(temp)
        return result