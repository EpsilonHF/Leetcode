"""
Suppose Andy and Doris want to choose a restaurant for dinner, 
and they both have a list of favorite restaurants represented 
by strings.

You need to help them find out their common interest with the 
least list index sum. If there is a choice tie between answers, 
output all of them with no order requirement. You could assume 
there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
"""

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = dict()
        d2 = dict()

        for i, e in enumerate(list1):
            d1[e] = i

        for i, e in enumerate(list2):
            d2[e] = i

        ret = []
        MIN = len(d1) + len(d2)

        for e in d1:
            if e in d2:
                index = d1[e] + d2[e]
                if index == MIN:
                    ret.append(e)
                elif index < MIN:
                    ret = [e]
                    MIN = index

        return ret
