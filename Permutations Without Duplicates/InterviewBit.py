class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def permutate(self, s, ans, perm):
		if len(s) == 0:
			perm.append(ans)
		else:
			for i in range(len(s)):
				ch = [s[i]]
				left = s[:i]
				right = s[i+1:]
				ans_mod = ans + ch
				s_mod = left + right
				self.permutate(s_mod, ans_mod, perm)
		return perm
	def permute(self, A):
		return self.permutate(A, [], [])
