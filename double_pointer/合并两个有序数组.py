# https://www.nowcoder.com/practice/89865d4375634fc484f3a24b7fe65665?tpId=295&tqId=658&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj%3Fpage%3D1%26tab%3D%25E7%25AE%2597%25E6%25B3%2595%25E7%25AF%2587%26topicId%3D295

class Solution:
    def merge(self , A, m, B, n):
        i = m - 1
        j = n - 1
        k = m+n-1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[k] = A[i]
                i -= 1
                k -= 1
            else:
                A[k] = B[j]
                j -= 1
                k -= 1
        while j >= 0:
            A[k] = B[j]
            k -= 1
            j -= 1
        return A

if __name__ == '__main__':
    pass