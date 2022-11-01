# https://leetcode.cn/problems/NUPfPr/

class Solution:
    def canPartition(self, nums) -> bool:
        su, n, m = sum(nums), len(nums), max(nums)
        s = su>>1
        if n<2 or su&1 or m>s:
            return False
        dp = [[False] * (s+1) for _ in range(n)]
        dp[0][0] = True
        dp[0][nums[0]] = True
        for i in range(1, n):
            for j in range(1, s+1):
                if nums[i] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][s]

# 以下为一维数组优化版
class Solution1:
    def canPartition(self, nums) -> bool:
        su, n, m = sum(nums), len(nums), max(nums)
        s = su>>1
        if n<2 or su&1 or m>s:
            return False
        dp = [False] * (s+1)
        dp[0] = True
        for i in range(1, n):
            for j in range(s, nums[i]-1, -1):
                dp[j] = dp[j] or dp[j-nums[i]]
        return dp[-1]

if __name__ == '__main__':
    nums = [1,5,11,9,56,73,43,86,8,3,32,57,7,76,42,54,5]
    print(Solution1().canPartition(nums))