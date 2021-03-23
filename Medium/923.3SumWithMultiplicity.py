'''
    Given an integer array arr, and an integer target, 
    return the number of tuples i, j, k such that i < j < k 
    and arr[i] + arr[j] + arr[k] == target.

    As the answer can be very large, return it modulo 10^9 + 7.

    Example:
    Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
    Output: 20
    Explanation: Enumerating by the values (arr[i], arr[j], arr[k]):
                 (1, 2, 5) occurs 8 times;
                 (1, 3, 4) occurs 8 times;
                 (2, 2, 4) occurs 2 times;
                 (2, 3, 3) occurs 2 times.

    Example:
    Input: arr = [1,1,2,2,2,2], target = 5
    Output: 12
    Explanation: arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
                 We choose one 1 from [1,1] in 2 ways,
                 and two 2s from [2,2,2,2] in 6 ways.

    Constraints:
        - 3 <= arr.length <= 3000
        - 0 <= arr[i] <= 100
        - 0 <= target <= 300
'''
#Difficuty: Medium
#71 / 71 test cases passed.
#Runtime: 88 ms
#Memory Usage: 14.4 MB

#Runtime: 88 ms, faster than 56.77% of Python3 online submissions for 3Sum With Multiplicity.
#Memory Usage: 14.4 MB, less than 77.44% of Python3 online submissions for 3Sum With Multiplicity.

from collections import Counter

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = 0
        counter = Counter(arr)
        arr = list(counter.keys())
        length = len(arr)
        modulo = 1000000007

        for i in range(length):
            for j in range(i, length):
                if target - arr[i] - arr[j] in counter:
                    if arr[i] == arr[j] == target-arr[i]-arr[j]:
                        count += counter[arr[i]] * (counter[arr[i]]-1) * (counter[arr[i]]-2) // 6
                    elif arr[i] == arr[j]:
                        count += counter[target-arr[i]-arr[j]] * (counter[arr[i]]) * (counter[arr[i]]-1) // 2
                    elif arr[i] < target-arr[i]-arr[j] and arr[j] < target-arr[i]-arr[j]:
                        count += counter[arr[i]] * counter[arr[j]] * counter[target-arr[i]-arr[j]]

        return count % modulo