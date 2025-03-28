from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        
        q = deque()
        q.append((root.left, root.right))

        while q:
            t1, t2 = q.popleft()

            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False

            q.append((t1.left, t2.right))
            q.append((t2.left, t1.right))

        return True