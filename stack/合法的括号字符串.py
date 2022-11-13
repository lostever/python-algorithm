class Solution:
    def isValidString(self , s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '*':
                stack.append(i)
                
            elif i == ')' and stack:
                j = -1
                if stack.count('('):
                    while stack[j] != '(':
                        j -= 1
                    stack.pop(j)
                else:
                    stack.pop()
            else:
                return False

        while stack.count('('):
            if stack.pop() == '*':
                stack.remove('(')
            else:
                return False
        return True
    

if __name__ == '__main__':
    a = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
    print(Solution().isValidString(a))