"""
1169. Invalid Transactions

A transaction is invalid if the amount exceeds $1000, or if it occurs within 60 minutes of another transaction with the same name in a different city. Return all invalid transactions.

Constraints:
- 1 <= transactions.length <= 1000
- Each transaction is a string in the format "name,time,amount,city"

Example:
Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]

"""
def invalidTransactions(transactions):
    res = set()
    trans = []
    for t in transactions:
        name, time, amount, city = t.split(',')
        trans.append((name, int(time), int(amount), city, t))
    for i, (name1, time1, amount1, city1, t1) in enumerate(trans):
        if amount1 > 1000:
            res.add(t1)
        for j, (name2, time2, amount2, city2, t2) in enumerate(trans):
            if i != j and name1 == name2 and city1 != city2 and abs(time1 - time2) <= 60:
                res.add(t1)
    return list(res)

# Example usage
if __name__ == "__main__":
    print(invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"]))
    # Output: ["alice,20,800,mtv","alice,50,100,beijing"]
