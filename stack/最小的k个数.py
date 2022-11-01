def GetLeastNumbers_Solution(input, k: int):
    res = []
    for _ in range(k):
        a = min(input)
        input.remove(a)
        res.append(a)
    return res
        
def quick_sort(l:list, start, end):
    if start >= end:
        return
    mid = l[start]
    left = start
    right = end
    while left < right:
        while l[right] >= mid and left < right:
            right -= 1
        l[left] = l[right]
        while l[left] < mid and left < right:
            left += 1
        l[right] = l[left]
    l[left] = mid

    quick_sort(l, start, left-1)
    quick_sort(l, right+1, end)

if __name__ == '__main__':
    input, k = [4,5,1,6,2,7,3,8],4
    # print(GetLeastNumbers_Solution(input, k))
    quick_sort(input, 0, len(input)-1)
    print(input)
