# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
请实现两个函数，用来分别序列化和反序列化二叉树。
如二叉树：
1
/ \
2 3
/ / \
4 5 6
其序列化就是： 1,2,4,$,$,$,3,5,$,$,6,$,$ 。

【解题思路】：
利用前序遍历的思想，当遇到None的时候，输出特殊字符代替。
同理，当反序列化时，也是按照前序遍历的思想，当发现该节点的下两个元素都是特殊符号时，表示该节点是叶子节点。
'''


# define the tree
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# print tree
def printTree(root):
    if not root:
        return
    print(root.val, end=",")
    printTree(root.left)
    printTree(root.right)


# Serialize a tree
def serializeTree(root, res):
    if not root:
        res.append("$")
        return

    res.append(root.val)
    serializeTree(root.left, res)
    serializeTree(root.right, res)


# Deserialize a tree
def deserializeTree(seria):
    if not seria:
        return None
    number = seria.pop(0)
    if isinstance(number, int):
        root = TreeNode(number)

        root.left = deserializeTree(seria)
        root.right = deserializeTree(seria)

        return root
    else:
        return None


# test
# 1. create a tree
def createTestSample():
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)
    D = TreeNode(4)
    E = TreeNode(5)
    F = TreeNode(6)
    A.left = B;
    A.right = C;
    B.left = D;
    C.left = E;
    C.right = F;

    return A


root = createTestSample()

# 2. test serialize tree
res = []
serializeTree(root, res)
print("1. pre-order traversal:")
printTree(root)
print("\n2. Serialize a Tree", res)
# 3. test deserialize a tree
deseriaTreeRoot = None
deseriaTreeRoot = deserializeTree(res)
print("3. After deserialization:")
printTree(deseriaTreeRoot)