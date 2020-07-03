"""
    Given an array of unique integers salary where salary[i] is the salary of 
    the employee i.
    Return the average salary of employees excluding the minimum and maximum 
    salary.

    Example:
    Input: salary = [4000,3000,1000,2000]
    Output: 2500.00000
    Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
    Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500

    Constraints:
        - 3 <= salary.length <= 100
        - 10^3 <= salary[i] <= 10^6
        - salary[i] is unique.
        - Answers within 10^-5 of the actual value will be accepted as correct.
"""
#Difficulty: Easy
#43 / 43 test cases passed.
#Runtime: 28 ms
#Memory Usage: 13.8 MB

#Runtime: 28 ms, faster than 88.54% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
#Memory Usage: 13.8 MB, less than 75.00% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.

class Solution:
    def average(self, salary: List[int]) -> float:
        mi = min(salary)
        ma = max(salary)
        l = len(salary) - 2
        return (sum(salary) - mi - ma) / l

#Runtime: 28 ms, faster than 88.54% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
#Memory Usage: 14 MB, less than 25.00% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.

class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)

#Runtime: 32 ms, faster than 75.38% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
#Memory Usage: 14 MB, less than 25.00% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(min(salary))
        salary.remove(max(salary))
        return sum(salary)/len(salary)    
