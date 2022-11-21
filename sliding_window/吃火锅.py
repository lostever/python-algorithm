def max_hp(l:list):
    fast = 0
    slow = 0
    right = -1
    left = -1
    cnt = float('-inf')
    while fast < len(l):
        while slow < fast and sum(l[slow: fast]) > cnt:
            cnt = sum(l[slow: fast])
            left = slow
            right = fast
            slow +=1
        fast += 1
        slow = 0
    return l[left: right]

if __name__ == '__main__':
    l = [2,5,7,-9,84,23,-33,7,98,-27]
    print(max_hp(l))

