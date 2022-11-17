# https://leetcode.cn/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid) -> int:
        def isrot(grid):
            for x in grid:
                for y in x:
                    if y == 1:
                        return False
            return True

        def change(x,y,l,l1,m,n):
            if l[x][y] == 1:
                for dx, dy in (0,1), (0,-1), (1,0), (-1,0):
                    if 0<=x+dx<m and 0<=y+dy<n and l[x+dx][y+dy]==2:
                        l1[x][y] = 2  # 注意这里是改变的另一个列表,原列表不变
                        return True
            return False
            
        m = len(grid)
        n = len(grid[0])
        res = 0
        while True:
            l1 = [[y for y in x] for x in grid]
            changed = False
            for x in range(m):
                for y in range(n): #下面函数传入另一个列表,原列表在比较完之前不能动
                    changed = change(x,y,grid,l1,m,n) or changed 
            if changed:
                res += 1
                grid = [[y for y in x] for x in l1]
            else:
                if isrot(grid):
                    return res
                else:
                    return -1

if __name__ == '__main__':
    a = [[2,1,1],[1,1,0],[0,1,1]]
    print(Solution().orangesRotting(a))
    