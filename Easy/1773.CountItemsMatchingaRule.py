'''
    You are given an array items, where each items[i] = 
    [typei, colori, namei] describes the type, color, and 
    name of the ith item. You are also given a rule 
    represented by two strings, ruleKey and ruleValue.

    The ith item is said to match the rule if one of the 
    following is true:
        - ruleKey == "type" and ruleValue == typei.
        - ruleKey == "color" and ruleValue == colori.
        - ruleKey == "name" and ruleValue == namei.

    Return the number of items that match the given rule.

    Example:
    Input: items = [["phone","blue","pixel"],
                    ["computer","silver","lenovo"],
                    ["phone","gold","iphone"]], 
           ruleKey = "color", 
           ruleValue = "silver"
    Output: 1
    Explanation: There is only one item matching the given 
                 rule, which is ["computer","silver","lenovo"].

    Example:
    Input: items = [["phone","blue","pixel"],
                    ["computer","silver","phone"],
                    ["phone","gold","iphone"]], 
           ruleKey = "type", 
           ruleValue = "phone"
    Output: 2
    Explanation: There are only two items matching the given 
                 rule, which are ["phone","blue","pixel"] and 
                 ["phone","gold","iphone"]. Note that the 
                 item ["computer","silver","phone"] does not 
                 match.

    Constraints:
        - 1 <= items.length <= 10^4
        - 1 <= typei.length, colori.length, namei.length, 
          ruleValue.length <= 10
        - ruleKey is equal to either "type", "color", or 
          "name".
        - All strings consist only of lowercase letters.
'''
#Difficulty: Easy
#92 / 92 test cases passed.
#Runtime: 244 ms
#Memory Usage: 20.6 MB

#Runtime: 244 ms, faster than 56.81% of Python3 online submissions for Count Items Matching a Rule.
#Memory Usage: 20.6 MB, less than 64.89% of Python3 online submissions for Count Items Matching a Rule.

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        description = {'type': 0, 'color': 1, 'name': 2}
        for item in items:
            if item[description[ruleKey]] == ruleValue:
                count += 1
        return count