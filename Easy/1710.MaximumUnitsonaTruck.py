'''
    You are assigned to put some amount of boxes onto one 
    truck. You are given a 2D array boxTypes, where 
    boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
        - numberOfBoxesi is the number of boxes of type i.
        - numberOfUnitsPerBoxi is the number of units in 
          each box of the type i.

    You are also given an integer truckSize, which is the 
    maximum number of boxes that can be put on the truck. 
    You can choose any boxes to put on the truck as long as 
    the number of boxes does not exceed truckSize.

    Return the maximum total number of units that can be put 
    on the truck.

    Example:
    Input: boxTypes = [[1,3],[2,2],[3,1]], 
           truckSize = 4
    Output: 8
    Explanation: There are:
                - 1 box of the first type that contains 3 
                  units.
                - 2 boxes of the second type that contain 2 
                  units each.
                - 3 boxes of the third type that contain 1 
                  unit each.
                - You can take all the boxes of the first 
                  and second types, and one box of the third 
                  type.
                - The total number of units will be 
                        = (1 * 3) + (2 * 2) + (1 * 1) = 8.

    Example:
    Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], 
           truckSize = 10
    Output: 91

    Constraints:
        - 1 <= boxTypes.length <= 1000
        - 1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
        - 1 <= truckSize <= 10^6
'''
#Difficulty: Easy
#76 / 76 test cases passed.
#Runtime: 148 ms
#Memory Usage: 14.9 MB

#Runtime: 148 ms, faster than 97.10% of Python3 online submissions for Maximum Units on a Truck.
#Memory Usage: 14.9 MB, less than 44.19% of Python3 online submissions for Maximum Units on a Truck.

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        units = 0
        boxes = {}
        for box, cap in boxTypes:
            if cap not in boxes:
                boxes[cap] = 0
            boxes[cap] += box
        sorted_boxes = sorted(boxes.keys(), reverse=True)
        for cap in sorted_boxes:
            if boxes[cap] <= truckSize:
                units += cap * boxes[cap]
                truckSize -= boxes[cap]
            else:
                units += cap * truckSize
                break
        return units
