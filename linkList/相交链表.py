# 优秀解法
class Solution:
    def getIntersectionNode(self, headA, headB):
        pA = headA
        pB = headB
        while pA != pB:
            pA = pA.next if pA else headB #遍历a如果到结尾了则指针指向b开头
            pB = pB.next if pB else headA #遍历b如果到结尾了则指针指向a开头
                                            # 当较长的链表指向较短的链表的开头时,
                                            # 长度差就消除了
        return pA
    
# 我的解法
class Solution1:
    def getIntersectionNode(self, headA, headB):
        idsa = set()
        while headA:
            idsa.add(id(headA))
            headA = headA.next
        while headB:
            if id(headB) in idsa:
                return headB
            headB = headB.next
        return None