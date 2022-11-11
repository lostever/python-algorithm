# https://www.nowcoder.com/practice/d11471c3bf2d40f38b66bb12785df47f?tpId=196&tqId=37088&rp=1&ru=/exam/oj&qru=/exam/oj&sourceUrl=%2Fexam%2Foj%3Fpage%3D2%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D196&difficulty=undefined&judgeStatus=undefined&tags=&title=

class Solution:
    def StrToInt(self , s: str) -> int:
        s = s.strip()
        t = ''
        n = 0
        if len(s) == 0: 
            return n
        if s[0] == '+' or s[0] == '-':
            t = s[0]
            s = s[1:]
        for i in s:
            if i.isdigit():
                t += i
                if int(t) < -2**31:
                    n = -2**31
                elif int(t) > 2**31-1:
                    n = 2**31-1
                else:
                    n = int(t)
            else:
                break
        return n