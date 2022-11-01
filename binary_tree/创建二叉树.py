class TreeNode(object):
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return str(self.data)
A, B, C, D, E, F, G, H, I = [TreeNode(x) for x in 'ABCDEFGHI']\

A.left = B
A.right = C
B.right = D
C.left = E
C.right = F
E.left = G
F.left = H
F.right = I

print(A.right)

