class Solution:
    def getLongestPalindrome(self , A: str) -> int:
        def func(s, n, start, end):
            while start >= 0 and end <= n-1 and s[start]==s[end]:
                start -= 1
                end += 1
            return end-start-1
        n = len(A)
        length = 1
        for i in range(n):
            length = max(func(A,n,i,i), func(A,n,i,i+1),length)
        return length


if __name__ == '__main__':
    A = "abaabababbabbabbababaaba"
    print(Solution().getLongestPalindrome(A))