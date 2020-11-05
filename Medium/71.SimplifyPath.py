"""
    Given an absolute path for a file (Unix-style), simplify it. Or in other 
    words, convert it to the canonical path.

    In a UNIX-style file system, a period . refers to the current directory. 
    Furthermore, a double period .. moves the directory up a level.

    Note that the returned canonical path must always begin with a slash /, 
    and there must be only a single slash / between two directory names. 
    The last directory name (if it exists) must not end with a trailing /. 
    Also, the canonical path must be the shortest string representing the 
    absolute path.

    Example:
    Input: "/home/"
    Output: "/home"
    Explanation: Note that there is no trailing slash after the last 
                 directory name.

    Example:
    Input: "/../"
    Output: "/"
    Explanation: Going one level up from the root directory is a no-op, as 
                 the root level is the highest level you can go.

    Example:
    Input: "/home//foo/"
    Output: "/home/foo"
    Explanation: In the canonical path, multiple consecutive slashes are 
                 replaced by a single one.

    Example:
    Input: "/a/./b/../../c/"
    Output: "/c"

    Example:
    Input: "/a/../../b/../c//.//"
    Output: "/c"

    Example:
    Input: "/a//b////c/d//././/.."
    Output: "/a/b/c"
"""
#Difficulty: Medium
#254 / 254 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.2 MB

#Runtime: 32 ms, faster than 65.76% of Python3 online submissions for Simplify Path.
#Memory Usage: 14.2 MB, less than 99.96% of Python3 online submissions for Simplify Path.

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = self.clearPath(path)
        for action in path:
            if action == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(action)
        return '/' + '/'.join(stack)

    def clearPath(self, path):
        path = path.split('/')
        i = 0
        while i < len(path):
            if path[i] == '.' or path[i] == '':
                path.pop(i)
                i = max(0, i-1)
                continue
            i += 1
        return path
