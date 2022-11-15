# https://www.nowcoder.com/practice/c466d480d20c4c7c9d322d12ca7955ac?tpId=196&rp=1&ru=%2Fexam%2Foj&qru=%2Fexam%2Foj&sourceUrl=%2Fexam%2Foj%3Ftab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D196&difficulty=&judgeStatus=&tags=&title=&gioEnter=menu

class Solution:
    def minWindow(self , S: str, T: str) -> str:
        def check(dict):
            for k, v in dict.items():
                if v < 0:
                    return False
            return True

        dic = {}
        for i in T:
            if i in dic:
                dic[i] -= 1
            else:
                dic[i] = -1
        
        cnt = len(S)+1
        slow = 0
        fast = 0
        left = -1
        right = -1
        while fast < len(S):
            c = S[fast]
            if c in dic:
                dic[c] += 1
            while check(dic):
                if cnt>fast-slow+1:
                    cnt = fast-slow+1
                    left = slow
                    right = fast
                c = S[slow]
                if c in dic: # 注意这里不能用 if dic.get(c) ,因为dic[c]的值为零, 将会被视为条件不成立
                    dic[c] -= 1 # 但是c确实在dic中,应该被视为条件成立, 因此要用if c in dic:
                slow += 1
            fast += 1
            
        if left == -1:
            return ''
        return S[left: right+1]

if __name__ == '__main__':
    S="XDOYEZODEYXNZ"
    T ="XYZ"
    print(Solution().minWindow(S,T))
