from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers
    @return: A list of unique permutations
    """
    def permutate(self, s, ans, perm):
        if len(s) == 0:
            perm.append(ans)
        else:
            d = set()
            for i in range(len(s)):
                ch = s[i]
                if ch not in d:
                    d.add(ch)
                    left = s[:i]
                    right = s[i+1:]
                    ans_mod = ans + [ch]
                    s_mod = left + right
                    self.permutate(s_mod, ans_mod, perm)
        return perm
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.permutate(nums, [], [])
