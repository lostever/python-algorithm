def quick_sort(alist, start, end):
    if start >= end:
        return
    mid = alist[start]
    left = start
    right = end
    while left < right:
        while mid <= alist[right] and left < right:
            right -= 1
        alist[left] = alist[right]
        while mid > alist[left] and left < right:
            left += 1
        alist[right] = alist[left]
    alist[left] = mid
    
    quick_sort(alist, start, left-1)
    quick_sort(alist, right+1, end)
        
if __name__ == '__main__':
    a = [5,7,9,8,6,4,1,3,8,9,2,0,78,39,23,14,3,6]
    n = len(a)-1
    quick_sort(a, 0, n)
    print(a)
    