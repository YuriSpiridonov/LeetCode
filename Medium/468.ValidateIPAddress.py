"""
    Write a function to check whether an input string is a valid IPv4 address 
    or IPv6 address or neither.

    IPv4 addresses are canonically represented in dot-decimal notation, which 
    consists of four decimal numbers, each ranging from 0 to 255, separated by 
    dots ("."), e.g.,172.16.254.1;
    Besides, leading zeros in the IPv4 is invalid. 
    For example, the address 172.16.254.01 is invalid.

    IPv6 addresses are represented as eight groups of four hexadecimal digits, 
    each group representing 16 bits. The groups are separated by colons (":"). 
    For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid 
    one. 
    Also, we could omit some leading zeros among four hexadecimal digits and 
    some low-case characters in the address to upper-case ones, 
    so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address
    (Omit leading zeros and using upper cases).
    However, we don't replace a consecutive group of zero value with a single 
    empty group using two consecutive colons (::) to pursue simplicity. 
    For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.
    Besides, extra leading zeros in the IPv6 is also invalid. 
    For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

    Example 1:
    Input: IP = "172.16.254.1"
    Output: "IPv4"
    Explanation: This is a valid IPv4 address, return "IPv4".

    Example 2:
    Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    Output: "IPv6"
    Explanation: This is a valid IPv6 address, return "IPv6".

    Constraints:
        - IP consists only of English letters, digits and the characters 
          "." and ":".
"""
#Difficulty: Medium
#73 / 73 test cases passed.
#Runtime: 24 ms
#Memory Usage: 14 MB

#Runtime: 24 ms, faster than 89.89% of Python3 online submissions for Validate IP Address.
#Memory Usage: 14 MB, less than 8.69% of Python3 online submissions for Validate IP Address.  

class Solution:

    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            IPv4 = IP.split('.')
            return self.validIPv4(IPv4)
        elif ':' in IP:
            IPv6 = IP.split(':')
            return self.validIPv6(IPv6)
        else:
            return 'Neither'

    def validIPv4(self, IPv4):
        if len(IPv4) == 4:
            for i in range(4):
                if not IPv4[i] or (IPv4[i][0] == '0' and len(IPv4[i]) > 1) or not IPv4[i].isdigit() or int(IPv4[i]) not in range(256):
                    return 'Neither'
            return 'IPv4'
        return 'Neither'

    def validIPv6(self, IPv6):
        valid_elements = {'1','2','3','4','5','6','7','8','9','0','a','A','b','B','c','C','d','D','e','E','f','F'}
        if len(IPv6) == 8:
            for i in range(8):
                if len(IPv6[i]) not in range(1, 5):
                    return 'Neither'
                for n in IPv6[i]:
                    if n not in valid_elements:
                        return 'Neither'
            return 'IPv6'
        return 'Neither'
