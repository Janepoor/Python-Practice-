# Binary Tree

class BinaryTree(object):

    def __init__(self, root_value):
        self.root = root_value
        self.leftchild = None
        self.rightchild = None

    # 插入左子树
    def insert_left(self, left_value):
        if self.leftchild == None:
            self.leftchild = BinaryTree(left_value)
        else:
            left_subtree = BinaryTree(left_value)
            left_subtree.leftchild = self.leftchild
            self.leftchild = left_subtree

    # 插入右子树
    def insert_right(self, right_value):
        if self.rightchild == None:
            self.rightchild = BinaryTree(right_value)
        else:
            right_subtree = BinaryTree(right_value)
            right_subtree.rightchild = self.rightchild
            self.rightchild = rightchild

    # 设置根节点的值
    def set_root(self, root_value):
        self.root = root_value

    # 获取根节点的值
    def get_root(self):
        return self.root

    # 获取左子树
    def get_leftchild(self):
        return self.leftchild

    # 获取右子树
    def get_rightchile(self):
        return self.rightchild




# tree traversal



def preorder(tree):
    if tree != None:
        print(tree.root)
        preorder(tree.leftchild)
        preorder(tree.rightchild)



def inorder(tree):
    if tree != None:
        inorder(tree.leftchild)
        print(tree.root)
        inorder(tree.rightchild)


def postorder(tree):
    if tree != None:
        postorder(tree.leftchild)
        postorder(tree.rightchild)
        print(tree.root)




