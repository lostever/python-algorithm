# https://www.nowcoder.com/practice/046a55e6cd274cffb88fc32dba695668?tpId=295&tags=&title=&difficulty=0&judgeStatus=0&rp=0&sourceUrl=%2Fexam%2Foj
class Solution:
    def solve(self , nums: str) -> int:
        
        if len(nums) == 0:
            return 0
        dp = [0] * (len(nums) + 1)
        dp[0] = 1
        for i in range(len(nums)):
            if nums[i] != '0':
                dp[i+1] += dp[i]
            if i > 0 and nums[i-1] != '0' and int(nums[i-1:i+1]) <= 26:
                dp[i+1] += dp[i-1]
        return dp[-1]
if __name__ == '__main__':
    print(Solution().solve('1225'))