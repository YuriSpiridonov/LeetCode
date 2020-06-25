"""
    You have a browser of one tab where you start on the homepage and you can 
    visit another url, get back in the history number of steps or move forward 
    in the history number of steps.

    Implement the BrowserHistory class:

        - BrowserHistory(string homepage) Initializes the object with the 
          homepage of the browser.
        - void visit(string url) visits url from the current page. It clears 
          up all the forward history.
        - string back(int steps) Move steps back in history. If you can only 
          return x steps in the history and steps > x, you will return only x 
          steps. Return the current url after moving back in history at most 
          steps.
        - string forward(int steps) Move steps forward in history. If you can 
          only forward x steps in the history and steps > x, you will forward 
          only x steps. Return the current url after forwarding in history at 
          most steps.

    Example:
    Input:
    ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
    [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
    Output:
    [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

    Explanation:
    BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
    browserHistory.visit("google.com");       // You are in "leetcode.com". 
                                              // Visit "google.com"
    browserHistory.visit("facebook.com");     // You are in "google.com". 
                                              // Visit "facebook.com"
    browserHistory.visit("youtube.com");      // You are in "facebook.com". 
                                              // Visit "youtube.com"
    browserHistory.back(1);                   // You are in "youtube.com", 
                                              // move back to "facebook.com" 
                                              // return "facebook.com"
    browserHistory.back(1);                   // You are in "facebook.com", 
                                              // move back to "google.com" 
                                              // return "google.com"
    browserHistory.forward(1);                // You are in "google.com", 
                                              // move forward to "facebook.com" 
                                              // return "facebook.com"
    browserHistory.visit("linkedin.com");     // You are in "facebook.com". 
                                              // Visit "linkedin.com"
    browserHistory.forward(2);                // You are in "linkedin.com", 
                                              // you cannot move forward any 
                                              // steps.
    browserHistory.back(2);                   // You are in "linkedin.com", 
                                              // move back two steps to 
                                              // "facebook.com" 
                                              // then to "google.com". return 
                                              // "google.com"
    browserHistory.back(7);                   // You are in "google.com", 
                                              // you can move back only one step 
                                              // to "leetcode.com". return 
                                              // "leetcode.com"

    Constraints:
        - 1 <= homepage.length <= 20
        - 1 <= url.length <= 20
        - 1 <= steps <= 100
        - homepage and url consist of  '.' or lower case English letters.
        - At most 5000 calls will be made to visit, back, and forward.
"""
#Difficulty: Medium
#71 / 71 test cases passed.
#Runtime: 332 ms
#Memory Usage: 16.2 MB

#Runtime: 332 ms, faster than 55.28% of Python3 online submissions for Design Browser History.
#Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Design Browser History.

class Node:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)
        
    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = new_node

    def back(self, steps: int) -> str:
        while steps >= 1:
            steps -= 1
            if self.current.prev is not None:
                self.current = self.current.prev
            else:
                break
        return self.current.homepage

    def forward(self, steps: int) -> str:
        while steps >= 1:
            steps -= 1
            if self.current.next is not None:
                self.current = self.current.next
            else:
                break
        return self.current.homepage


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
