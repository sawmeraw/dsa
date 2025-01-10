class TreeNode():

    def init(self, val, left=None, right = None):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = TreeNode(val)
        if self.root == None:
            self.root = new_node
            return

        curr = self.root
        parent = None

        while curr:
            parent = curr
            if val > curr.val:
                curr = curr.right
            elif val < curr.val:
                curr = curr.left

        if val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        return self.root


    def insert_recursive(self,root, val):

        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insert_recursive(root.right, val)
        elif val < root.val:
            root.left = self.insert_recursive(root.left, val)

        return root

    def remove(self,root, val):
        if not root:
            return None

        if val > root.val:
            root.right = self.remove(root, val)
        elif val < root.val:
            root.left = self.remove(root, val)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.minValueNode(root.right)
                root.val = minNode.val
                root.right = self.remove(root.right, minNode.val)

        return root


    def minValueNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr






