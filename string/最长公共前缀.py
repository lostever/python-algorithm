# https://www.nowcoder.com/practice/28eb3175488f4434a4a6207f6f484f47?tpId=295&tags=&title=&difficulty=0&judgeStatus=0&rp=0&sourceUrl=%2Fexam%2Foj
from typing import List


class Solution:
    def longestCommonPrefix(self , strs: List[str]) -> str:
        if not strs:
            return ''
        s = list(sorted(strs,key=len))[0] 

        for i in strs:
            while i[:len(s)] != s:
                s = s[:-1]
        return s
