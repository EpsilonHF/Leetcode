"""
Find the minimum length word from a given dictionary words, 
which has all the letters from the string licensePlate. Such 
a word is said to complete the given string licensePlate

Here, for letters we ignore case. For example, "P" on the 
licensePlate still matches "p" on the word.

It is guaranteed an answer exists. If there are multiple answers, 
return the one that occurs first in the array.

The license plate might have the same letter occurring multiple 
times. For example, given a licensePlate of "PP", the word "pair" 
does not complete the licensePlate, but the word "supper" does.

Example 1:
Input: 
licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
Output: "steps"
Explanation: 
The smallest length word that contains the letters "S", "P", "S", and "T".
Note that the answer is not "step", because the letter "s" must 
occur in the word twice.
Also note that we ignored case for the purposes of comparing 
whether a letter exists in the word.
"""

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plate = [s.lower() for s in licensePlate if s.isalpha()]

        for word in sorted(words, key = len):
            temp = plate[:]
            for c in word:
                if c in temp:
                    del temp[temp.index(c)]
            if len(temp) == 0:
                return word
