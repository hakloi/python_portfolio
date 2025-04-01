from collections import deque

class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        q = deque([(root, root.val)])

        while q:
            node, summ = q.popleft()

            if node.left is not None:
                q.append((node.left, summ + node.left.val))
            if node.right is not None:
                q.append((node.right, summ + node.right.val))
            if node.left is None and node.right is None and summ == targetSum:
                return True
        return False

        

        