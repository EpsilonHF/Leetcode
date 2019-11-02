"""
Given a string containing only digits, restore it by returning all 
possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res = []
        self.dfs(s, [], 0, res)
        
        return res
    
        
    def dfs(self, s, path, n, res):
        if n > 4:
            return
        
        if len(s) == 0:
            if n == 4:
                res.append('.'.join(path))
            return
        
        if s[0] == '0':
            self.dfs(s[1:], path+['0'], n+1, res)
            return        
        
        index = min(len(s), 3)
        for i in range(1, index+1):
            if int(s[:i]) <= 255:
                self.dfs(s[i:], path + [s[:i]], n+1, res)
