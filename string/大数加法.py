# https://www.nowcoder.com/practice/11ae12e8c6fe48f883cad618c2e81475?tpId=295&tags=&title=&difficulty=0&judgeStatus=0&rp=0&sourceUrl=%2Fexam%2Foj

class Solution:
    def solve(self , s: str, t: str) -> str:
        if not s:
            if not t:
                return '0'
            else:
                return t
        else:
            if not t:
                return s
            else:
                return str(int(s) + int(t))
                
                