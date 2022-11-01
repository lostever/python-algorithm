class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
# 
# @param root TreeNode类 
# @param o1 int整型 
# @param o2 int整型 
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self , root , o1 , o2 ):
        # write code here
        def dfs(root, o1, o2):
            if not root:
                return None
            if root.val ==o1 or root.val==o2:
                return root
            left = dfs(root.left, o1, o2)
            right = dfs(root.right, o1, o2)
            if not left:
                return right
            if not right:
                return left
            return root
        return dfs(root, o1, o2).val

# 下面是我的做法,超内存
class Solution1:
    def lowestCommonAncestor(self , root: TreeNode, o1: int, o2: int) -> int:
        def path(root, k, res):
            if not root:
                return []
            res.append(root.val)
            if root.val == k:
                return res
            return path(root.left, k, res[:]) or path(root.right, k, res[:])
            
        res1, res2 = [], []
        s1 = path(root, o1, res1)
        s2 = path(root, o2, res2)
        f = None
        for a,b in zip(s1, s2):
            if a == b:
                f = a
            else:
                break
        return f
            