#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 计算模板串S在文本串T中出现了多少次
# @param S string字符串 模板串
# @param T string字符串 文本串
# @return int整型
#
class Solution:
    def nextl(self, s):
        next = [0]
        prefix_len = 0
        i = 1
        while i< len(s):
            if s[i] == s[prefix_len]:
                i += 1
                prefix_len += 1
                next.append(prefix_len)
            else:
                if prefix_len == 0:
                    next.append(0)
                    i += 1
                else:
                    prefix_len = next[prefix_len-1]
        return next
    def kmp(self , S , T ):
        i = 0
        j = 0
        nex_ar = self.nextl(S)
        cnt = 0
        while i < len(T):
            if T[i] == S[j]:
                i += 1
                j += 1
                if j == len(S):
                    cnt += 1
            elif j > 0:
                j = nex_ar[j-1]
            else:
                i += 1
                j = 0
        return cnt

        
if __name__ == '__main__':
    a = 'ababac'
    print(Solution().nextl(a))
    print(Solution().kmp(a, 'ababababac'))