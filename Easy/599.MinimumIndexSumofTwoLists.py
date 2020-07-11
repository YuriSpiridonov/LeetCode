"""
    Suppose Andy and Doris want to choose a restaurant for dinner, and they 
    both have a list of favorite restaurants represented by strings.

    You need to help them find out their common interest with the least list i
    ndex sum. If there is a choice tie between answers, output all of them with 
    no order requirement. You could assume there always exists an answer.

    Note:
        1. The length of both lists will be in the range of [1, 1000].
        2. The length of strings in both lists will be in the range of [1, 30].
        3. The index is starting from 0 to the list length minus 1.
        4. No duplicates in both lists.
"""
#Difficulty: Easy
#133 / 133 test cases passed.
#Runtime: 348 ms
#Memory Usage: 13.9 MB

#Your runtime beats 19.17 % of python3 submissions.
#Your memory usage beats 93.00 % of python3 submissions.

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        for i, restaurant in enumerate(list1):
            if restaurant in list2:
                index_sum = i + list2.index(restaurant)
                if index_sum not in d:
                    d[index_sum] = [restaurant]
                else:
                    d[index_sum].append(restaurant)
        return d[min(d.keys())]
