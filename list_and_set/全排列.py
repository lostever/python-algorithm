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
            
# 有重复项全排列(严重超时)
def dfs(num, visited:dict, row=[], res={}):
    if len(row) == len(num):
        res[str(row[:])] = None
        return 
    for i in num:
        if visited[i]:
            visited[i] -= 1
            row.append(i)
            dfs(num, visited, row, res)
            row.pop()
            visited[i] += 1

if __name__ == '__main__':
    num = [1,2,3,4,5,6,7,8]
    num.sort()
    visited = {}
    res = {}
    for i in num:
        if i in visited:
            visited[i] += 1
        else:
            visited[i] = 1
    
    dfs(num, visited=visited, res=res)
    # res = [eval(x) for x in res.keys()]
    print(res)
    print(len(res))