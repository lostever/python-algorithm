# https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337?tpId=13&tqId=11169&ru=/exam/oj

# 优秀解法
def Merge(self, pHead1, pHead2):
        # write code here
        dummy = cur = ListNode(0)  # 设置一个头节点,任意值
        while pHead1 and pHead2:
            if pHead1.val <pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 =pHead2.next
            cur = cur.next
        cur.next = pHead1 or pHead2
        return dummy.next

# 我的解法
class Solution:
    def Merge(self , pHead1: ListNode, pHead2: ListNode) -> ListNode:
        node1 = pHead1
        node2 = pHead2
        if not node1:
            return node2
        if not node2:
            return node1

        head = None
        pre = None
        if node1.val <= node2.val:
            head = node1
            pre = node1
            node1 = node1.next
        else:
            head = node2
            pre = node2
            node2 = node2.next

        while node1 or node2:
            if not node1:
                pre.next = node2
                return head
            if not node2:
                pre.next = node1
                return head
            
            if node1.val <= node2.val:
                pre.next = node1
                pre = node1
                node1 = node1.next
            else:
                pre.next = node2
                pre = node2
                node2 = node2.next
            