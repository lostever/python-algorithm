# https://www.nowcoder.com/practice/55fb3c68d08d46119f76ae2df7566880?tpId=295&tags=&title=&difficulty=0&judgeStatus=0&rp=0&sourceUrl=%2Fexam%2Foj

class Solution:
    def solve(self , IP: str) -> str:
        def ipv4(l):
            for i in l:
                if i and i.isdigit() and i[0]!='0' and int(i) <= 255:
                    continue
                else:
                    return 'Neither'
            return 'IPv4'
        def ipv6(l):
            for i in l:
                if 0 < len(i) <= 4 and i.isalnum():
                    for x in i:
                        if x.isalpha() and x.upper() > "F":
                            return "Neither"
                        else:
                            continue
                else:
                    return 'Neither'
            return 'IPv6'
        
        li = IP.split('.')
        if len(li) == 4:
            return ipv4(li)
        else:
            li = IP.split(':')
            if len(li) == 8:
                return ipv6(li)
            else:
                return 'Neither'
