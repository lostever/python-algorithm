# 我的代码
# 递归函数解决
def tfp(list:list, num):
    if len(list) == 1:
        return list[0] == num
    for i in range(len(list)):
        list.append(list.pop(0))
        if tfp(list[1:], num+list[0]) or tfp(list[1:], num-list[0]) \
            or tfp(list[1:], num*list[0]) or tfp(list[1:], num/list[0]):
            return True
    else:
        return False

        
# 第一名的代码
def func(nums, tar):
    if len(nums) == 1: return nums[0] == tar
    # 注意各种计算顺序都要考虑
    for i in range(len(nums)):
        nums = nums[1:] + [nums[0]]
        if func(nums[1:], tar+nums[0]) or func(nums[1:], tar-nums[0]) or func(nums[1:], tar*nums[0]) or func(nums[1:], tar/nums[0]):
            return True
    return False
    
l = [7, 2, 1, 10]
print(tfp(l, 24))
        