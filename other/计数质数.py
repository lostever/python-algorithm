# https://leetcode.cn/problems/count-primes/description/

# 埃氏筛
class Solution:
    def countPrimes(self, n: int) -> int:
        cnt = 0
        if n == 1 or n == 0:
            return 0
        l = [True] * n
        l[0] = False
        l[1] = False
        for i in range(2, int(n**0.5)+1):
            if l[i]:
                for j in range(i*i, n, i):
                    l[j] = False
        cnt = l.count(True)
        return cnt


if __name__ == '__main__':
    n = int(1e8)
    print(Solution().countPrimes(n))