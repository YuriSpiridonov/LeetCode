'''
    There is a hidden integer array arr that consists of n 
    non-negative integers.

    It was encoded into another integer array encoded of 
    length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1]. 
    For example, if arr = [1,0,2,1], then encoded = [1,2,3].

    You are given the encoded array. You are also given an 
    integer first, that is the first element of arr, i.e. 
    arr[0].

    Return the original array arr. It can be proved that 
    the answer exists and is unique.

    Example:
    Input: encoded = [1,2,3], first = 1
    Output: [1,0,2,1]
    Explanation: If arr = [1,0,2,1], then first = 1 and 
                 encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = 
                 [1,2,3]

    Example:
    Input: encoded = [6,2,7,3], first = 4
    Output: [4,2,0,7,4]

    Constraints:
        - 2 <= n <= 10^4
        - encoded.length == n - 1
        - 0 <= encoded[i] <= 10^5
        - 0 <= first <= 10^5
'''
#Difficuly: Easy
#76 / 76 test cases passed.
#Runtime: 252 ms
#Memory Usage: 16 MB

#Runtime: 252 ms, faster than 100.00% of Python3 online submissions for Decode XORed Array.
#Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Decode XORed Array.

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        i = 0
        length = len(encoded)
        while i < length:
            arr.append(arr[i] ^ encoded[i])
            i += 1
        return arr
