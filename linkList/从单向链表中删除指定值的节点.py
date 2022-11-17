# https://www.nowcoder.com/practice/f96cd47e812842269058d483a11ced4f?tpId=37&tags=&title=&difficulty=&judgeStatus=&rp=1&sourceUrl=%2Fexam%2Foj%2Fta%3Fdifficulty%3D1%26page%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&gioEnter=menu

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


class linkList():
    def __init__(self, node=None):
        self.head = node

    def travel(self):
        if not self.head:
            return None
        cur = self.head
        while cur:
            print(cur.val, end=' ')
            cur = cur.next

    def insert(self, val, k):
        cur = self.head
        while cur.val != k:
            cur = cur.next
        node = Node(val)
        node.next = cur.next
        cur.next = node
            
    def delete(self, val):
        cur = self.head
        pre = None
        while cur.val != val:
            pre = cur
            cur = cur.next
        if not pre:
            self.head = self.head.next
        else:
            pre.next = cur.next


if __name__ == '__main__':
        
    s = input().split()
    N = s.pop(0)
    node = Node(s.pop(0))
    d = s.pop()
    link = linkList(node)
    while s:
        val = s.pop(0)
        k = s.pop(0)
        link.insert(val, k)

    link.delete(d)
    link.travel()