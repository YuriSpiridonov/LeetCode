"""
    Given a valid (IPv4) IP address, return a defanged version of that IP address.
    A defanged IP address replaces every period "." with "[.]".
    
    Example:
    Input: address = "1.1.1.1"
    Output: "1[.]1[.]1[.]1"

    Constraints:
        - The given address is a valid IPv4 address.
"""
#Difficulty: Easy
#62 / 62 test cases passed.
#Runtime: 48 ms
#Memory Usage: 13.9 MB

#Runtime: 48 ms, faster than 6.22% of Python3 online submissions for Defanging an IP Address.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Defanging an IP Address.
        
import re
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return re.sub("\.", "[.]", address)
