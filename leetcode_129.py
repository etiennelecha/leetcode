from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    '''
    Leetcode medium. Find the sum of all traversal paths. Yes I realy wanted to use
    the yield syntax. Not it's not optimal
    OC et MC linear. 
    '''
def sumNumbers(self, root: Optional[TreeNode]) -> int:
    def dfs(acc: int, node: Optional[TreeNode]) -> int:
        if not node:
            yield 0
        elif not node.left and not node.right:
            yield 10 * acc + node.val
        else:    
            yield from dfs(10 * acc + node.val, node.right)
            yield from dfs(10 * acc + node.val, node.left)

    return sum(dfs(0, root))

class OptimalSolution:
    '''
    Faster because we sum as we traverse the tree (Beats ~88% time, ~95% mem)
    '''
def sumNumbers(self, root: Optional[TreeNode]) -> int:
    def dfs(acc, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        elif not node.left and not node.right:
            return 10 * acc + node.val
        else:    
            return dfs(10 * acc + node.val, node.left) + dfs(10 * acc + node.val, node.right)
    return dfs(0, root)