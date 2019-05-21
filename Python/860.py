"""
At a lemonade stand, each lemonade costs $5.

Customers are standing in a queue to buy from you, and order 
one at a time (in the order specified by bills).

Each customer will only buy one lemonade and pay with either a 
$5, $10, or $20 bill. You must provide the correct change to each 
customer, so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Return true if and only if you can provide every customer with 
correct change.

Example 1:

Input: [5,5,5,10,20]
Output: true
Explanation:
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0, 10:0, 20:0}

        for bill in bills:
            change[bill] += 1
            if bill == 10:
                change[5] -= 1

                if change[5] < 0:
                    return False

            if bill == 20:
                change[5] -= 1
                if change[10]:
                    change[10] -= 1
                else:
                    change[5] -= 2

                if change[5] < 0:
                    return False

        return True
