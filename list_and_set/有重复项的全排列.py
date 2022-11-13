class Solution:
    def permutation(self, S: str):
        def dfs(res, used, s, ans=''):
            if len(ans) == len(s):
                res.append(ans)
                return
            for i in range(len(s)):
                if i > 0 and s[i] == s[i-1] and not used[i-1]:
                    continue
                if not used[i]:
                    used[i] = 1
                    dfs(res, used, s, ans+s[i])
                    used[i] = 0

        s = ''.join(sorted(S))  ##一定要先对字符串排序
        res = []
        used = [0] * len(s)
        dfs(res, used, s)
        return res
    
if __name__ == '__main__':
    a = 'qqe'
    print(Solution().permutation(a))