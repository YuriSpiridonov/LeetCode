"""
    Given an array of strings names of size n. You will create n folders in your 
    file system such that, at the ith minute, you will create a folder with the 
    name names[i].

    Since two files cannot have the same name, if you enter a folder name which 
    is previously used, the system will have a suffix addition to its name in 
    the form of (k), where, k is the smallest positive integer such that the 
    obtained name remains unique.

    Return an array of strings of length n where ans[i] is the actual name the 
    system will assign to the ith folder when you create it.

    Example:
    Input: names = ["gta","gta(1)","gta","avalon"]
    Output: ["gta","gta(1)","gta(2)","avalon"]
    Explanation: Let's see how the file system creates folder names:
                 "gta" --> not assigned before, remains "gta"
                 "gta(1)" --> not assigned before, remains "gta(1)"
                 "gta" --> the name is reserved, system adds (k), 
                           since "gta(1)" is also reserved, systems put k = 2. 
                           it becomes "gta(2)"
                 "avalon" --> not assigned before, remains "avalon"

    Constraints:
        - 1 <= names.length <= 5 * 10^4
        - 1 <= names[i].length <= 20
        - names[i] consists of lower case English letters, digits and/or round 
          brackets.
"""
#Difficulty: Medium
#33 / 33 test cases passed.
#Runtime: 400 ms
#Memory Usage: 32.4 MB

#Runtime: 400 ms, faster than 86.53% of Python3 online submissions for Making File Names Unique.
#Memory Usage: 32.4 MB, less than 100.00% of Python3 online submissions for Making File Names Unique.

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        files = {}
        new_names = []
        for name in names:
            if name not in files:
                files[name] = [0]
                new_names.append(name)
            else:
                number = files[name][-1] + 1
                new_name = name + '(' + str(number) + ')'
                while new_name in files:
                    number += 1
                    new_name = name + '(' + str(number) + ')'
                files[new_name] = [0]
                files[name].append(number)
                new_names.append(new_name)
        return new_names
