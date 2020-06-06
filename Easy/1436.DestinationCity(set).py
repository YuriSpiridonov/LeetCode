"""
    You are given the array paths, where paths[i] = [cityAi, cityBi] means 
    there exists a direct path going from cityAi to cityBi. Return the 
    destination city, that is, the city without any path outgoing to another city.
    
    It is guaranteed that the graph of paths forms a line without any loop, 
    therefore, there will be exactly one destination city.
    
    Example:
    Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    Output: "Sao Paulo" 
    Explanation: Starting at "London" city you will reach "Sao Paulo" city 
    which is the destination city. Your trip consist of: 
        "London" -> "New York" -> "Lima" -> "Sao Paulo".
    
    Constraints:
        - 1 <= paths.length <= 100
        - paths[i].length == 2
        - 1 <= cityAi.length, cityBi.length <= 10
        - cityAi != cityBi
        - All strings consist of lowercase and uppercase English letters and 
          the space character.
"""
#Difficulty: Easy
#103 / 103 test cases passed.
#Runtime: 60 ms
#Memory Usage: 13.7 MB

#Runtime: 60 ms, faster than 45.65% of Python3 online submissions for Destination City.
#Memory Usage: 13.7 MB, less than 94.11% of Python3 online submissions for Destination City.

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        departure = set()
        arrival = set()
        for path in paths:
            departure.add(path[0])
            arrival.add(path[1])
        for destination in arrival:
            if destination not in departure:
                return destination
