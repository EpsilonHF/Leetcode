"""
Given a list of sorted characters letters containing only lowercase 
letters, and given a target letter target, find the smallest 
element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' 
and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"
"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target == 'z':
            return letters[0]

        start, end = 0, len(letters) - 1
        while start <= end:
            mid = (start + end) // 2
            if letters[mid] > target:
                if mid == 0 or letters[mid-1] <= target:
                    return letters[mid]
                else:
                    end = mid - 1
            else:
                start = mid + 1

        return letters[0]
