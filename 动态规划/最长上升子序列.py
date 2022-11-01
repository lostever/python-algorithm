# https://www.nowcoder.com/practice/5164f38b67f846fb8699e9352695cd2f?tpId=295&tags=&title=&difficulty=0&judgeStatus=0&rp=0&sourceUrl=%2Fexam%2Foj

from typing import List


class Solution:
    def LIS(self , arr: List[int]) -> int:
        if not arr: return 0
        n = len(arr)
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if arr[j] < arr[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
    
