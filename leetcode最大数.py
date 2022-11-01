nums = [3,30,34,5,9]
class Solution:
    def largestNumber(self, nums: list[int]):
        l = list(map(str, nums))
        c = len(l)
        for i in range(c):
            for j in range(i+1, c):
                if l[i]+l[j] < l[j]+l[i]:
                    l[j], l[i] = l[i], l[j]
        for i in l:
            print(i,end='')
            
            
if __name__ == '__main__':
    
    a = Solution()
    a.largestNumber(nums)
