def ThreeSum(num):
    res = []
    if not num:
        return res
    num.sort()
    for i in range(len(num)):
        j = i+1
        k = len(num)-1
        while j < k:
            if num[j]+num[k] > -num[i]:
                k -= 1
            elif num[j]+num[k] < -num[i]:
                j += 1
            else:
                l = [num[i], num[j], num[k]]
                if l not in res:
                    res.append(l)
                j += 1
    return res

if __name__ == '__main__':
    print(ThreeSum([-2,0,0,2,2]))