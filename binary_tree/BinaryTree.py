# 将'遍历二叉树.py'文件拷贝成为'BinaryTree'模组,以供'BinarySearchTree.py'导入

from collections import deque
class TreeNode(object):
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return str(self.data)
    
    
def create_tree():
    A, B, C, D, E, F, G, H, I = [TreeNode(x) for x in 'ABCDEFGHI']\

    A.left = B
    A.right = C
    B.right = D
    C.left = E
    C.right = F
    E.left = G
    F.left = H
    F.right = I
    return A

# 先序遍历, 递归
def preOder(node):
    if not node:
        return
    print(node)
    preOder(node.left)
    preOder(node.right)

# 中序遍历, 递归
def inOder(node):
    if not node:
        return
    inOder(node.left)
    print(node)
    inOder(node.right)

# 后序遍历, 递归
def postOder(node):
    if not node:
        return
    postOder(node.left)
    postOder(node.right)
    print(node)

# 先序遍历,迭代器
def preOderIter(root):
    node = root
    s = []
    while True:
        while node:
            print(node)
            s.append(node)
            node = node.left
        if not s:
            break
        node = s.pop().right

# 层序遍历
def levelOder(root):
    q = deque([root])
    while q:
        node = q.popleft()
        print(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        
# 求二叉树深度, 层序遍历法改造
def depth(node):
    q = deque([(node, 1)])
    while q:
        node, d = q.popleft()
        if node.left:
            q.append((node.left, d + 1))
        if node.right:
            q.append((node.right , d + 1))
    return d

# 求树深度, 递归法
def depth2(node):
    if not node:
        return 0
    tl = depth2(node.left)
    tr = depth2(node.right)
    return max(tl, tr) + 1

# 拷贝树,递归法
def copyTree(node):
    if not node:
        return None
    lt = copyTree(node.left)
    rt = copyTree(node.right)
    return TreeNode(node.data, lt, rt)

if __name__ == '__main__':

    root = create_tree()
    # postOder(root)
    # levelOder(root)
    
    # print(depth(root))
    # print(depth2(root))

    # copyRt = copyTree(root)
    # levelOder(copyRt)

