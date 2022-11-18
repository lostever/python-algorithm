# https://www.nowcoder.com/practice/762836f4d43d43ca9deb273b3de8e1f4?tpId=13&tqId=11198&ru=/exam/oj

class Solution:
    def IsContinuous(self , numbers) -> bool:
        n0 = numbers.count(0)    # 找出0的个数
        for _ in range(n0):      # 去掉零
            numbers.remove(0)
        numbers.sort()           # 排序
        cnt = 0
        for i in range(1,len(numbers)):
            if numbers[i] == numbers[i-1]: # 如果出现相同的数,则返回False
                return False               # 即不能构成顺子
            cnt += numbers[i] - numbers[i-1] # 计算相邻两个数的差值
            cnt -= 1                         # 减去一之后再累加
        if cnt <= n0:           # 如果超过1的差值和大于0 的个数,则返回False
            return True
        else:
            return False 
