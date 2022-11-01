# https://www.lintcode.com/problem/1431/
class Solution:
    """
    @param dominoes: a string
    @return: a string representing the final state
    """
    def push_dominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        dom_next = dom[:]
        d = dominoes.count('.')
        while d:
            dpre = d
            if dom[0]=='.' and dom[1]=='L':
                dom_next[0] = 'L'
                d -= 1
            if dom[-1]=='.' and dom[-2]=='R':
                dom_next[-1] = 'R'
                d -= 1
            for i in range(1,len(dom)-1):
                if dom[i]=='.' and (dom[i-1]!='.' or dom[i+1]!='.'):
                    if dom[i-1]=='R' and dom[i+1]=='.':
                        dom_next[i] = 'R'
                        d -= 1
                    elif dom[i-1]=='.' and dom[i+1]=='L':
                        dom_next[i] = 'L'
                        d -= 1
                    elif dom[i-1]=='L' and dom[i+1]=='L':
                        dom_next[i] = 'L'
                        d -= 1
                    elif dom[i-1]=='R' and dom[i+1]=='R':
                        dom_next[i] = 'R'
                        d -= 1
            if dpre == d:
                break
            dom = dom_next[:]
        return ''.join(dom)