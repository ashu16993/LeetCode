'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check_symmetry(root_left,root_right):
            # if root_left is None and root_right is None:
            #     return True
            try:
                bool_left,bool_right = False,False
                if root_left.left is None and root_right.right is None:
                    bool_left = True
                elif root_left.left.val==root_right.right.val:
                    bool_left = check_symmetry(root_left.left,root_right.right)
                    
                if root_left.right is None and root_right.left is None:
                    bool_right = True
                elif root_left.right.val==root_right.left.val:
                    bool_right = check_symmetry(root_left.right,root_right.left)
                
                return bool_left and bool_right
            except Exception as e:
                # print(e)
                return False

        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        try:
            if root.left.val == root.right.val:
                return check_symmetry(root.left,root.right)
            else:
                return False
        except:
            return False