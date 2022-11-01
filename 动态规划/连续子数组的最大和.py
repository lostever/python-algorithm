# https://www.nowcoder.com/practice/459bd355da1549fa8a49e350bf3df484?tpId=295&tqId=23259&ru=%2Fpractice%2F459bd355da1549fa8a49e350bf3df484&qru=%2Fta%2Fformat-top101%2Fquestion-ranking&sourceUrl=%2Fexam%2Foj
from typing import List


class Solution:
    def FindGreatestSumOfSubArray(self , array: List[int]) -> int:
        n = len(array)
        dp = [0] * n
        dp[0] = array[0]
        for i in range(1,n):
                dp[i] = max(array[i], dp[i-1]+array[i])
        return max(dp)

if __name__ == '__main__':
    array = [1,-2,3,10,-4,7,2,-5]
    print(Solution().FindGreatestSumOfSubArray(array))