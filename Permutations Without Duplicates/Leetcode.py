class Solution:
    def permutate(self, s, ans, perm):
        if len(s) == 0:
            perm.append(ans)
        else:
            for i in range(len(s)):
                ch = s[i]
                left = s[:i]
                right = s[i+1:]
                s_mod = left + right
                ans_mod = ans + [ch]
                self.permutate(s_mod, ans_mod, perm)
        return perm
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.permutate(nums, [], [])
