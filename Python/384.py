"""
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any 
// permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""

class Solution:

    def __init__(self, nums: List[int]):
        self.data = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.data

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        A = self.data[:]
        for i in range(len(A)):
            j = random.randint(i, len(A)-1)
            A[i], A[j] = A[j], A[i]
        return A



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
