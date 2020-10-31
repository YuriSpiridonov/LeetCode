"""
    A transaction is possibly invalid if:
        - the amount exceeds $1000, or;
        - if it occurs within (and including) 60 minutes of another transaction 
          with the same name in a different city.

    Each transaction string transactions[i] consists of comma separated values 
    representing the name, time (in minutes), amount, and city of the 
    transaction.

    Given a list of transactions, return a list of transactions that are 
    possibly invalid.  You may return the answer in any order.

    Example:
    Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
    Output: ["alice,20,800,mtv","alice,50,100,beijing"]
    Explanation: The first transaction is invalid because the second 
                 transaction occurs within a difference of 60 minutes, have 
                 the same name and is in a different city. Similarly the 
                 second one is invalid too.

    Example:
    Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
    Output: ["alice,50,1200,mtv"]

    Example:
    Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
    Output: ["bob,50,1200,mtv"]

    Constraints:
        - transactions.length <= 1000
        - Each transactions[i] takes the form "{name},{time},{amount},{city}"
        - Each {name} and {city} consist of lowercase English letters, and have 
          lengths between 1 and 10.
        - Each {time} consist of digits, and represent an integer between 0 
          and 1000.
        - Each {amount} consist of digits, and represent an integer between 0 
          and 2000.
"""
#Difficulty: Medium
#33 / 33 test cases passed.
#Runtime: 640 ms
#Memory Usage: 14.6 MB

#Runtime: 640 ms, faster than 19.77% of Python3 online submissions for Invalid Transactions.
#Memory Usage: 14.6 MB, less than 49.87% of Python3 online submissions for Invalid Transactions.

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        db = {}
        possibly_invalid = []
        for transaction in transactions:
            name, time, amount, location = transaction.split(',')
            if name not in db:
                db[name] = [time], [amount], [location]
            else:
                for i in range(len(db[name][0])):
                    if abs(int(time) - int(db[name][0][i])) <= 60 and location != db[name][2][i]:
                        prev = name+','+db[name][0][i]+','+db[name][1][i]+','+db[name][2][i]
                        if prev not in possibly_invalid:
                            possibly_invalid.append(prev)
                        if transaction not in possibly_invalid:
                            possibly_invalid.append(transaction)
                db[name][0].append(time)
                db[name][1].append(amount)
                db[name][2].append(location)
            if int(amount) > 1000 and transaction not in possibly_invalid:
                possibly_invalid.append(transaction)
        return possibly_invalid
