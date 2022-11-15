# 无重复项全排列
def qpl(num, visited=set(), row=[], res=[]):
    if len(row) == len(num):
        res.append(row[:])
        return
    for i in num:
        if i not in visited:
            visited.add(i)
            row.append(i)
            qpl(num, visited, row, res)
            row.pop()
            visited.remove(i)
            
# 有重复项全排列
def dfs(res, used, s, ans=[]):
    if len(ans) == len(s):
        res.append(ans)
        return
    for i in range(len(s)):
        if i > 0 and s[i] == s[i-1] and not used[i-1]:
            continue
        if not used[i]:
            used[i] = 1
            dfs(res, used, s, ans[:]+[s[i]])
            used[i] = 0

    # s = ''.join(sorted(S))  ##一定要先对字符串排序
    # res = []
    # used = [0] * len(s)
    # dfs(res, used, s)
    # return res
    
if __name__ == '__main__':
    num = [1,2,3,4,6,4,6,4,6,5,6,7,8]
    num.sort()
    res = []

    used = [0] * len(num)
    
    dfs(res, used, num)

    print(res)
    print(len(res))