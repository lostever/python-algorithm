# https://www.nowcoder.com/practice/3911a20b3f8743058214ceaa099eeb45?tpId=295&tags=&title=&difficulty=0&judgeStatus=0&rp=0&sourceUrl=%2Fexam%2Foj
from typing import List


class Solution:
    def minMoney(self , arr: List[int], aim: int) -> int:
        n = len(arr)
        dp = [float('inf')]*(aim+1)
        dp[0] = 0
        for i in range(n):
            for j in range(arr[i],aim+1):
                dp[j] = min(dp[j], dp[j-arr[i]]+1)
        return dp[-1] if dp[-1] != float('inf') else -1  # type: ignore
            
            
if __name__ == '__main__':
    arr = [5,3,2,3,7,9,21,13,11]
    aim = 244
    print(Solution().minMoney(arr,aim))