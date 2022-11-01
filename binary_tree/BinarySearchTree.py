from collections import deque
from BinaryTree import TreeNode, levelOder


class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def search(self, k):
        node, parent = self._search(k)
        return node
        
    def _search(self, k):
        parent = None
        node = self.root
        while node and node.data != k:
            parent = node
            if k < node.data:
                node = node.left
            else:
                node = node.right
        return node, parent
                
    def insert(self, k):
        node, parent = self._search(k)
        if node:
            return
        if not parent:
            self.root = TreeNode(k)
        elif k < parent.data:
            parent.left = TreeNode(k)
        else: 
            parent.right = TreeNode(k)
             

    # def delete(self, k):
    #     node, parent = self._search(k)
    #     if not node:
    #         return
    #     elif parent:
    #         if k < parent.data:
                
                
if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(1)
    bst.insert(1)
    bst.insert(8)
    bst.insert(12)
    bst.insert(2)
    levelOder(bst.root)
    
        
