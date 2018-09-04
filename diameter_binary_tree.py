'''
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def distance_from_root_left(self,root):
    #     if root.left is None:
    #         return 0
    #     else:
    #         return (self.distance_from_root_left(root.left) + 1)
    # def distance_from_root_right(self,root):
    #     if root.right is None:
    #         return 0
    #     else:
    #         return (self.distance_from_root_right(root.right) + 1)
    # def distance_from_root(self,root):
    #     return self.distance_from_root_right(root)+self.distance_from_root_left(root)
    def get_depth(self,root):
        if root is None:
            return 0
        else:
            left = self.get_depth(root.left)
            right = self.get_depth(root.right)
            self.distance = max(self.distance, left+right+1)
        return max(left,right)+1
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        # return self.distance_from_root(root)
        else:
            self.distance = 0
            depth = self.get_depth(root)
            return self.distance-1