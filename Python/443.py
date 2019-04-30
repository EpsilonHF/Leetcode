"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than 
or equal to the original array.

Every element of the array should be a character (not int) 
of length 1.

After you are done modifying the input array in-place, return 
the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should 
be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is 
replaced by "c3".
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        read = write = 0
        l = len(chars)

        while read < l:
            ch = chars[read]
            count = 0

            while read < l and chars[read] == ch:
                read += 1
                count += 1

            chars[write] = ch
            write += 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write
