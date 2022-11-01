class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        used = set()
        dp = [0] * n
        for i in range(n):
            if s[i] not in used:
                dp[i] = 1
                used.add(s[i])
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                dp[i] = (dp[i] + dp[j]) % (10**9+7)
                if s[i] == s[j]:
                    break
        return sum(dp)
   
if __name__ == '__main__':
    s = 'abc'
    print(Solution().distinctSubseqII(s))