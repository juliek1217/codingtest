# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        op_list = []
        queue = [root]
        while queue:
            level_len = len(queue)
            temp_list = []
            for i in range(level_len):
                node = queue.pop(0)
                temp_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            op_list.append(temp_list)
        return op_list
