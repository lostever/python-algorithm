# https://www.nowcoder.com/practice/c3120c1c1bc44ad986259c0cf0f0b80e?tpId=295&tags=&title=&difficulty=0&judgeStatus=0&rp=0&sourceUrl=%2Fexam%2Foj
class Solution:
    def trans(self , s: str, n: int) -> str:
        res = s.split(' ')
        res.reverse()
        for i in range(len(res)):
            res[i] = list(res[i])  # type: ignore
            for j in range(len(res[i])):
                if res[i][j].isupper():
                    res[i][j] = res[i][j].lower()  # type: ignore
                else:
                    res[i][j] = res[i][j].upper()  # type: ignore
            res[i] = ''.join(res[i])
        res = ' '.join(res)
        return res

if __name__ == '__main__':
    s = 'h e' 
    n = 3
    print(Solution().trans(s,n))    