"""
A binary watch has 4 LEDs on the top which represent the hours 
(0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant 
bit on the right.

For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of 
LEDs that are currently on, return all possible times the watch 
could represent.

Example:

Input: n = 1
Return: 
["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
"""

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:

        def dfs(n, hour, minute, idx):
            if hour > 11 or minute > 59:
                return None
            if n == 0:
                res.append(str(hour) + ":" + "0" * (minute<10) + str(minute))
                return None
            for i in range(idx, 10):
                if i < 4:
                    dfs(n - 1, hour | (1 << i), minute, i + 1)
                else:
                    k = i - 4
                    dfs(n - 1, hour, minute | (1 << k), i + 1)

        res = []
        dfs(num, 0, 0, 0)

        return res
