s = input()
l = []

for i in range(1, len(s)):
    p = s[i]
    q = ''
    n = 1
    m = 0
    while i-n>=0 and i+n<=len(s)-1 and s[i-n] == s[i+n]:
        p = s[i-n] + p + s[i+n]
        n += 1
    if p != s[i]:
        l.append(p)
    while i-m>=0 and i+m+1<=len(s)-1 and s[i-m] == s[i+m+1]:
        q = s[i-m]+q+s[i+m+1]
        m += 1
    if q:
        l.append(q)
l.sort(key=len)
print(len(l[-1]))

'''
描述
给定一个仅包含小写字母的字符串，求它的最长回文子串的长度。
所谓回文串，指左右对称的字符串。
所谓子串，指一个字符串删掉其部分前缀和后缀（也可以不删）的字符串
数据范围：字符串长度1\le s\le 350\1≤s≤350 
进阶：时间复杂度：O(n)\O(n) ，空间复杂度：O(n)\O(n) 
输入描述：
输入一个仅包含小写字母的字符串

输出描述：
返回最长回文子串的长度

示例1
输入：
cdabbacc
复制
输出：
4
复制
说明：
abba为最长的回文子串 
'''