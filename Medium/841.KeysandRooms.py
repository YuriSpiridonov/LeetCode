'''
    There are N rooms and you start in room 0.  Each room 
    has a distinct number in 0, 1, 2, ..., N-1, and each 
    room may have some keys to access the next room. 

    Formally, each room i has a list of keys rooms[i], and 
    each key rooms[i][j] is an integer in [0, 1, ..., N-1] 
    where N = rooms.length.  A key rooms[i][j] = v opens the 
    room with number v.

    Initially, all the rooms start locked (except for room 0). 

    You can walk back and forth between rooms freely.

    Return true if and only if you can enter every room.

    Example:
    Input: [[1],[2],[3],[]]
    Output: true
    Explanation: - We start in room 0, and pick up key 1.
                 - We then go to room 1, and pick up key 2.
                 - We then go to room 2, and pick up key 3.
                 - We then go to room 3.  Since we were able 
                   to go to every room, we return true.

    Example:
    Input: [[1,3],[3,0,1],[2],[0]]
    Output: false
    Explanation: We can't enter the room with number 2.

    Note:
        1. 1 <= rooms.length <= 1000
        2. 0 <= rooms[i].length <= 1000
        3. The number of keys in all rooms combined is at 
           most 3000.
'''
#Difficulty: Medium
#67 / 67 test cases passed.
#Runtime: 64 ms
#Memory Usage: 14.5 MB

#Runtime: 64 ms, faster than 78.84% of Python3 online submissions for Keys and Rooms.
#Memory Usage: 14.5 MB, less than 99.84% of Python3 online submissions for Keys and Rooms.

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        length = len(rooms)
        queue = [0]
        visited = set()
        while queue:
            key = queue.pop(0)
            if key not in visited:
                visited.add(key)
                queue.extend(rooms[key])
        return len(visited) == length