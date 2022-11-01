# https://www.lintcode.com/problem/305/
from typing import (
    List,
)

class Solution:
    """
    @param matrix: A matrix
    @return: An integer.
    """
    def longest_increasing_path(self, matrix: List[List[int]]) -> int:
        d = {}
        m, n = len(matrix), len(matrix[0])

        def find(x,y):
            if d.get((x,y)):
                return d[(x,y)]
            res = 1
            for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                if 0<=x+dx<m and 0<=y+dy<n and matrix[x][y]<matrix[x+dx][y+dy]:
                    res = max(find(x+dx,y+dy)+1, res)
            d[(x,y)] = res
            return res
        b = 0
        for x in range(m):
            for y in range(n):
                b = max(find(x,y), b)
        return b