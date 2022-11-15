# https://leetcode.cn/problems/number-of-longest-increasing-subsequence/description/

class Solution(object):
    def findNumberOfLIS(self, nums):
        N = len(nums)
        if N <= 1:
            return N
        length = [1] * N
        count = [1] * N

        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] >= length[i]:
                        length[i] = max(length[i], 1 + length[j])
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

        longest = max(length)
        return sum(c for i, c in enumerate(count) if length[i] == longest)

if __name__ == '__main__':
    a = [2,2,2,2,2]
    print(Solution().findNumberOfLIS(a))