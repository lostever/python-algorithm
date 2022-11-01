from typing import (
    List,
)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Solution:
    """
    @param l: The length of the matrix
    @param w: The width of the matrix
    @param points: three points 
    @return: The sum of the paths sum
    """
    def calculation_the_sum_of_path(self, l: int, w: int, points: List[Point]) -> int:

        def num_of_path(l:list):
            x, y = l
            if x < 0 or y < 0:
                return 0
            if x == 0 or y == 0:
                return 1
            dp = [[1]*(x+1)] + [[0]*(x+1) for _ in range(y)]
            for i in range(1,y+1):
                dp[i][0] = dp[i-1][0]
                for j in range(1,x+1):
                    dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000007
            return dp[-1][-1]

        points.sort(key=lambda i: i.x)
        a, b, c = points
        MOD = 1000000007

        bl = [b.x-a.x, b.y-a.y]
        cl = [c.x-b.x, c.y-b.y]
        al = [a.x-1, a.y-1]
        dl = [l-c.x, w-c.y]

        an = num_of_path(al)
        bn = num_of_path(bl)
        cn = num_of_path(cl)
        dn = num_of_path(dl)

        return an*bn%MOD*cn%MOD*dn%MOD
            
if __name__ == '__main__':
    l = 1
    w = 5
    points = [Point(1,2),Point(1,3),Point(1,4)]
    print(Solution().calculation_the_sum_of_path(l,w,points))
    
    
    
