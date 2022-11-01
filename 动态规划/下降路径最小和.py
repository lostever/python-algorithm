# https://www.lintcode.com/problem/1711/description

from typing import (
    List,
)

class Solution:
    """
    @param a: the given array
    @return: the minimum sum of a falling path
    """
    def min_falling_path_sum(self, a: List[List[int]]) -> int:
        x = len(a)
        dp = a[0][:]
        for i in range(1, x):
            tmp = [0]*x
            tmp[0] = min(dp[0], dp[1]) + a[i][0]
            tmp[-1] = min(dp[-2], dp[-1]) + a[i][-1]
            for j in range(1, x-1):
                tmp[j] = min(dp[j-1], dp[j], dp[j+1]) + a[i][j]
            dp = tmp
        return min(dp)