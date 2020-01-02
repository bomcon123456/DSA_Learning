class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        queue = collections.deque()
        queue.append(root)
        queue.append(root)
        while len(queue) > 0:
            left = queue.popleft()
            right = queue.popleft()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True

    def isSymmetric_recur(self, root):
        def isMirror(left,right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return (left.val == right.val) and isMirror(left.left,
                    right.right) and isMirror(left.right, right.left)

        return isMirror(root, root)
